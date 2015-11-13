#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
#################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

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
from classifyAB import classify

clf = classify(features_train, labels_train, 50, 1)

pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

print("Accuracy: " + str(acc))






try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
