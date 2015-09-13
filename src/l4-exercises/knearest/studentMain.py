#!/usr/bin/python

""" (rahaugh) my attempt at k nearest neighbour """

import sys
from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from classifyKN import classify

features_train, labels_train, features_test, labels_test = makeTerrainData()


# (rahaugh) 1 gives the highest accuracy 0.94 but looks very overfitted
# 2 - 100 or so all yield 0.928 and look proggressively smoother
# even higher values start to get worse accuracy
clf = classify(features_train, labels_train, 1)

pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

print("Accuracy: " + str(acc))

#### grader code, do not modify below this line

prettyPicture(clf, features_test, labels_test)
#output_image("test.png", "png", open("test.png", "rb").read())