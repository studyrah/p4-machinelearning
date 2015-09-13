#!/usr/bin/python

""" (rahaugh) my attempt at random forest """

import sys
from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from classifyRF import classify

features_train, labels_train, features_test, labels_test = makeTerrainData()


''' (rahaugh) 
default (n_estimators = 10, min_samples_split = 2)

n_estimators   min_samples_split   accuracy
-------------  -----------------   --------
1              2                   0.9 (very overfitted)
5              2                   0.908
10             2                   0.92
20             2                   0.912
50             2                   0.916
500            2                   0.92   (gets smoother - less overfitted)
5000           2                   0.92
10             5                   0.928
10             10                  0.924
10             25                  0.92
10             50                  0.92
10             100                 0.888

'''
clf = classify(features_train, labels_train, 10, 5)

pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

print("Accuracy: " + str(acc))

#### grader code, do not modify below this line

prettyPicture(clf, features_test, labels_test)
#output_image("test.png", "png", open("test.png", "rb").read())