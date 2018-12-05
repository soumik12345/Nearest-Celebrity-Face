import cv2, os
import numpy as np

def preprocess_database(location):
    for file in os.listdir(location):
        img = cv2.resize(cv2.imread(location + file), (96, 96))
        cv2.imwrite(location + file, img)

def preprocess_testcases(location):
    for file in os.listdir(location):
        img = cv2.resize(cv2.imread(location + file), (96, 96))
        cv2.imwrite(location + file, img)