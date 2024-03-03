# -*- coding: utf-8 -*-
"""final_fp_gender.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k7jFSSiPVcv4qpy2HZadggf5dh95GDyE
"""

import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf

import os
import cv2

import matplotlib.pyplot as plt

import joblib

model=joblib.load('/content/drive/MyDrive/fp_model.joblib')

xtest=cv2.imread('//content//1__M_Left_index_finger.BMP', cv2.IMREAD_GRAYSCALE)#fp scanner jekhane image save korbe sei directory r path

img_resize = cv2.resize(xtest, (96, 96))
img_resize = img_resize.reshape(1, 96, 96, 1)
ytest=model.predict(img_resize)
ytest = (ytest >= 0.5).astype(np.int32)
print(ytest)
print(ytest.ndim)
print(ytest.shape)
print(ytest[0][0])

if ytest[0][0] ==0:
     txt="Male"

with open('my_file.txt', 'w') as file:
    print(txt, file=file)