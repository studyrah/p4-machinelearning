#!/usr/bin/python

import sys
import pickle
from outlier_cleaner import outlierCleaner
from add_features import addFeatures

sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import test_classifier, dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi',
  'salary', 'bonus']


### Load the dictionary containing the dataset
data_dict = pickle.load(open("final_project_dataset.pkl", "r") )

### Task 2: Remove outliers

data_dict = outlierCleaner(data_dict)

### Task 3: Create new feature(s)

data_dict = addFeatures(data_dict)

### Store to my_dataset for easy export below.

my_dataset = data_dict

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

from sklearn.svm import SVC
clf = SVC(kernel="linear")

import numpy as np
features = np.array([[  201955.,  4175000.],
 [ 477.,    0.],
 [  267102.,  1200000.],
 [ 239671.,  400000.],
 [ 80818.,      0.],
 [ 231330.,  700000.],
 [  213999.,  5249999.],
 [ 216582.,       0.],
 [ 187922.,  250000.],
 [  213625.,  1000000.],
 [ 248546.,  850000.],
 [  278601.,  1350000.],
 [ 248017.,  500000.],
 [ 261516.,  750000.],
 [ 330546.,  900000.],
 [  240189.,  1250000.],
 [ 261809.,  300000.],
 [  415189.,  1000000.],
 [  288542.,  1200000.],
 [ 314288.,  800000.],
 [ 184899.,  325000.],
 [ 206121.,  600000.],
 [  365163.,  3000000.],
 [ 492375.,  800000.],
 [ 210500.,  425000.],
 [ 250100.,  600000.],
 [  262788.,  1000000.],
 [ 221003.,   70000.],
 [ 278601.,  800000.],
 [ 210692.,  750000.],
 [ 182245.,  200000.],
 [ 170941.,  350000.],
 [  304588.,  2500000.],
 [  440698.,  1300000.],
 [ 199157.,  350000.],
 [ 1060932.,  2000000.],
 [ 192008.,  509870.],
 [ 231946.,  850000.],
 [ 274975.,  600000.],
 [ 272880.,  750000.],
 [ 6615.,     0.],
 [  374125.,  1150000.],
 [  243293.,  1500000.],
 [ 262663.,  700000.],
 [  211788.,  1700000.],
 [ 130724.,       0.],
 [ 85274.,      0.],
 [ 288558.,  250000.],
 [ 275101.,  400000.],
 [  404338.,  1000000.],
 [ 174246.,       0.],
 [  271442.,  3100000.],
 [ 309946.,  700000.],
 [ 224305.,  800000.],
 [  339288.,  8000000.],
 [ 1072321.,  7000000.],
 [  273746.,  1000000.],
 [ 236457.,  200000.],
 [ 349487.,       0.],
 [ 263413.,  900000.],
 [  365038.,  1100000.],
 [  370448.,  2600000.],
 [ 365788.,  600000.],
 [ 267093.,  325000.],
 [  251654.,  1100000.],
 [ 229284.,  400000.],
 [ 329078.,  750000.],
 [ 94941.,      0.],
 [  261879.,  1000000.],
 [ 655037.,  300000.],
 [ 197091.,  400000.],
 [ 96840.,      0.],
 [  76399.,  100000.],
 [  420636.,  1750000.],
 [ 249201.,  700000.],
 [  304110.,  2000000.],
 [ 269076.,  650000.],
 [ 248146.,  600000.],
 [ 211844.,  200000.],
 [  428780.,  1500000.],
 [ 1111258.,  5600000.],
 [ 239502.,  500000.],
 [ 162779.,  100000.],
 [ 257486.,  700000.],
 [ 265214.,  600000.],
 [ 222093.,       0.],
 [ 247338.,  300000.],
 [ 26704229.,  97343619.],
 [ 288589.,  788750.],
 [ 357091.,  850000.],
 [ 259996.,  325000.],
 [ 63744.,      0.],
 [  510364.,  3000000.],
 [ 317543.,  450000.],
 [ 158403.,       0.]])

labels = np.array([0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0,
 1.0,
 1.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 1.0,
 1.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 1.0,
 1.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 1.0]
)

featurest = np.array([[  201955.,  4175000.],
 [ 477.,    0.],
 [  267102.,  1200000.],
 [ 239671.,  400000.],
 [ 80818.,      0.],
 [ 231330.,  700000.],
 [  213999.,  5249999.],
 [ 216582.,       0.],
 [ 187922.,  250000.],
 [  213625.,  1000000.]])


labelst = np.array([0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 1.0,
 0.0,
 0.0,
 0.0])



clf.fit(featurest, labelst)
predictions = clf.predict(features)

from sklearn.metrics import accuracy_score
print accuracy_score(predictions, labels)

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script.
### Because of the small size of the dataset, the script uses stratified
### shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

#test_classifier(clf, my_dataset, features_list)

### Dump your classifier, dataset, and features_list so 
### anyone can run/check your results.

#dump_classifier_and_data(clf, my_dataset, features_list)