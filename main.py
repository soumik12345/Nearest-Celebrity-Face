print("Importing Libraries")
from keras.models import Sequential
from keras.layers import Conv2D, ZeroPadding2D, Activation, Input, concatenate
from keras.models import Model
from keras.layers.normalization import BatchNormalization
from keras.layers.pooling import MaxPooling2D, AveragePooling2D
from keras.layers.merge import Concatenate
from keras.layers.core import Lambda, Flatten, Dense
from keras.initializers import glorot_uniform
from keras.engine.topology import Layer
from keras import backend as K
K.set_image_data_format('channels_first')
import cv2, os, random, shutil
import numpy as np
from numpy import genfromtxt
import pandas as pd
import tensorflow as tf
from fr_utils import *
from inception_blocks_v2 import *
from preprocess import *
np.set_printoptions(threshold = np.nan)

# Triplet Loss Function
def triplet_loss(y_true, y_pred, alpha = 0.2):
    anchor, positive, negative = y_pred[0], y_pred[1], y_pred[2]
    pos_dist = tf.reduce_sum(tf.square(anchor - positive), axis=-1)
    neg_dist = tf.reduce_sum(tf.square(anchor - negative), axis=-1)
    basic_loss = pos_dist - neg_dist + alpha
    loss = tf.reduce_sum(tf.maximum(basic_loss, 0.0))
    return loss

# Geometrical Distance between Images
def find_distance(image_path, identity, database, model):
    encoding = img_to_encoding(image_path, model)
    dist = np.linalg.norm(encoding - database[identity])
    return dist

# Preprocess Images in a location
def create_datadict(database_location, model):
    data_dict = {}
    for celeb in os.listdir(database_location):
        data_dict.update({ celeb : img_to_encoding(database_location + celeb, model) })
    return data_dict

def find_image_distances(image_location, database, model):
    dist_dict = {}
    for id in database.keys():
        dist = find_distance(image_location, id, database, model)
        dist_dict.update({ id : dist })
    return dist_dict

def display_image(image_loc, name):
    fig, axes = plt.subplots(1, 2, figsize = (18, 5))
    fig.subplots_adjust(hspace = 0.5, wspace = 0.5)
    for i, ax in enumerate(axes.flat):
        ax.imshow(cv2.cvtColor(cv2.imread(image_loc[i]), cv2.COLOR_BGR2RGB))
        ax.set_xlabel(name[i])
        ax.set_xticks([])
        ax.set_yticks([])
    plt.show()

# Main function
def main():
    print("Loading Face Recognition Model ....")
    FRmodel = faceRecoModel(input_shape = (3, 96, 96))
    print("Compiling Face Recognition Model ....")
    FRmodel.compile(optimizer = 'adam', loss = triplet_loss, metrics = ['accuracy'])
    print("Loading Weights for Face Recognition Model ....")
    load_weights_from_FaceNet(FRmodel)
    preprocess_database("./Database/Images/")
    print("Generating Database of Available Images")
    database = create_datadict("./Database/Images/", FRmodel)
    preprocess_testcases("./Testcases/Preprocessed/")
    for file in os.listdir("./TestCases/Preprocessed/"):
        dist_dict = find_image_distances("./TestCases/Preprocessed/" + file, database, FRmodel)
        celeb_filename = min(dist_dict, key = dist_dict.get)
        celeb = celeb_filename.split('.')[0]
        display_image(
            ["./TestCases/Actual/" + file, "./Database/Celebs/" + celeb_filename],
            [file.split(".")[0], celeb]
        )

# Driver Code
main()