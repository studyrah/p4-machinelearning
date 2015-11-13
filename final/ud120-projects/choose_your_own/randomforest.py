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

from classifyRF import classify

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




try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
