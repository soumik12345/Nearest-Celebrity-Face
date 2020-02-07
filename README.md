# Nearest-Celebrity-Face

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/facenet-a-unified-embedding-for-face/face-verification-on-ijb-c)](https://paperswithcode.com/sota/face-verification-on-ijb-c?p=facenet-a-unified-embedding-for-face)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/facenet-a-unified-embedding-for-face/face-verification-on-labeled-faces-in-the)](https://paperswithcode.com/sota/face-verification-on-labeled-faces-in-the?p=facenet-a-unified-embedding-for-face)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/facenet-a-unified-embedding-for-face/face-verification-on-megaface)](https://paperswithcode.com/sota/face-verification-on-megaface?p=facenet-a-unified-embedding-for-face)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/facenet-a-unified-embedding-for-face/face-identification-on-megaface)](https://paperswithcode.com/sota/face-identification-on-megaface?p=facenet-a-unified-embedding-for-face)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/facenet-a-unified-embedding-for-face/face-verification-on-youtube-faces-db)](https://paperswithcode.com/sota/face-verification-on-youtube-faces-db?p=facenet-a-unified-embedding-for-face)

### Overview
Implementation of [FaceNet: A Unified Embedding for Face Recognition and Clustering
](https://arxiv.org/abs/1503.03832v3) to find the celebrity whose face matches the closest to yours.
The input face is encoded with a pretrained inception model into a vector and then its geometric distance is calculated with the encoded vectors of all the images present in the dataset and the image with the least distance is selected.

**Article Link:** [http://geekyrakshit.com/deep-learning/nearest-celebrity-face/](http://geekyrakshit.com/deep-learning/nearest-celebrity-face/)

### Installation
1. Create a new conda environment using `conda create --name nearest_celeb_face`
2. Activate the `activate nearest_celeb_face` if you are on Windows and `source activate nearest_celeb_face` if you are on Linux
3. Clone the repository using `git clone https://github.com/soumik12345/Nearest-Celebrity-Face`
4. Enter the root directory using `cd Nearest-Celebrity-Face`
5. Install the required dependencies using `pip install -r requirements.txt`

### Usage
The `TestCases` folder contains two folders `Actual` that contains full sized images of individuals and `Preprocessed` containing the faces manually cropped out of the full sized images. Any number of testcases can be added provided that one image each is present in the `Actual` and `Preprocessed` folders with the exact same filename and the preprocessed image should have the face manually cropped out for best performance. Refer to the already cropped images for further detail on how to crop. Once the tescases are setup, run `python main.py` or `python3 main.py` to run the program.

### Sample Outputs
![](https://github.com/soumik12345/Nearest-Celebrity-Face/blob/master/Results/Figure_1-1.png)
![](https://github.com/soumik12345/Nearest-Celebrity-Face/blob/master/Results/Figure_1-3.png)
![](https://github.com/soumik12345/Nearest-Celebrity-Face/blob/master/Results/Figure_1-5.png)
![](https://github.com/soumik12345/Nearest-Celebrity-Face/blob/master/Results/Figure_1-8.png)
![](https://github.com/soumik12345/Nearest-Celebrity-Face/blob/master/Results/Figure_1.png)
![](https://github.com/soumik12345/Nearest-Celebrity-Face/blob/master/Results/Figure_1-10.png)
