#!/usr/bin/python

""" (rahaugh) my attempt at ada boost """

import sys
from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from classifyAB import classify

features_train, labels_train, features_test, labels_test = makeTerrainData()


''' (rahaugh) 

default n_estimators = 50
default learning_rate = 1

increasing n_estimators makes it more accurate to the training set and 
therefore makes it overfitted

(adjust n_estimators in isolation) (default learning_rate = 1)

n_estimators   accuracy (on test set)
------------   ----------------------
1              0.74 (note this is a straight vertical line - which is I guess what you'd expect from a decision tree with one decision)
2              0.804 (2 boxes)
3              0.888
10             0.916
50             0.924
100            0.924 (but more eratic due to overfitting)
1000           0.916 (even more so)

(adjust learning_rate in isolation) (default n_estimators = 50)

learning_rate    accuracy
-------------    --------
1                0.924
2                0.924 (but more overfitted)
10               0.336 (all classified as 'fast')
0.1              0.916 (less overfitted)
0.5              0.924
'''
clf = classify(features_train, labels_train, 50, 1)

pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

print("Accuracy: " + str(acc))

#### grader code, do not modify below this line

prettyPicture(clf, features_test, labels_test)
#output_image("test.png", "png", open("test.png", "rb").read())