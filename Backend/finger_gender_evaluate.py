# -*- coding: utf-8 -*-
"""finger_gender_evaluate.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KMC40yL-EYPNIKF1ryXjuspBC7r6QyE9
"""

import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf

import os
import cv2

import matplotlib.pyplot as plt

def extract_label(img_path,underscore_flag ):
    filename, _ = os.path.splitext(os.path.basename(img_path))

    subject_id, etc = filename.split('__')

    if underscore_flag:
      gender, finger, _, _, _ = etc.split('_')
    else:
      gender, finger, _, _ = etc.split('_')

    gender = 0 if gender == 'M' else 1

    return np.array([gender], dtype=np.uint16)

def loading_data(path,boolean):
    data = []
    for img in os.listdir(path):
            img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
            img_resize = cv2.resize(img_array, (96,96))
            label = extract_label(os.path.join(path, img),boolean)

            data.append([label[0], img_resize ])

    return data

path='/content/drive/MyDrive/male'

data=loading_data(path,False)

number_of_elements = len(data)

print("Number of elements in the list:", number_of_elements)

img, labels = [], []
for label, feature in data:
    labels.append(label)
    img.append(feature)

x_test,y_test= [], []

x_test = np.array(img).reshape(-1, 96, 96, 1)
y_test = np.array(labels)
print(x_test.ndim)
print(x_test.shape)
print(y_test.ndim)
print(y_test.shape)

x_test2 = x_test/255
y_test2 = y_test
print(x_test.ndim)
print(x_test.shape)
print(y_test.ndim)
print(y_test.shape)
print(x_test2[0])

import joblib

model=joblib.load('/content/drive/MyDrive/fp_model.joblib')

model.evaluate(x_test,y_test)

model.evaluate(x_test2,y_test2)

predictions = model.predict(x_test)

print(predictions.ndim)
print(predictions.shape)

predictions2 = model.predict(x_test2)
print(predictions2.ndim)
print(predictions2.shape)

print(predictions[0])

print(predictions2[0])

predictions = (predictions >= 0.5).astype(np.int32)

print(predictions)

male_cnt=0
female_cnt=0
for gender in np.nditer(predictions):
    if gender ==0:
     print("Male",end=" ")
     male_cnt+=1
    else:
     print("Female",end=" ")
     female_cnt+=1
print("\n males predicted:",male_cnt)
print("\n females predicted:",female_cnt)

acc=(male_cnt/number_of_elements)*100
print("accuracy is:",acc)

predictions2 = (predictions2 >= 0.5).astype(np.int32)

print(predictions2)

male_cnt2=0
female_cnt2=0
for gender in np.nditer(predictions2):
    if gender ==0:
     print("Male",end=" ")
     male_cnt2+=1
    else:
     print("Female",end=" ")
     female_cnt2+=1
print("\n males predicted:",male_cnt2)
print("\n females predicted:",female_cnt2)

acc2=(male_cnt2/number_of_elements)*100
print("accuracy is:",acc2)#Male folder e onek kota bhul kore female copy hoye bose ache