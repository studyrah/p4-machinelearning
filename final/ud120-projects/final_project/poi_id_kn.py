#!/usr/bin/python

import sys
import pickle
from time import time
import copy

from outlier_cleaner import outlierCleaner
from add_features import addFeatures
from rescale_features import rescale

sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import test_classifier, dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".

features_filename = sys.argv[1]

features_list = [line.rstrip('\n') for line in open(features_filename)]  
  
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

from sklearn import neighbors

k = 3
clf = neighbors.KNeighborsClassifier(n_neighbors=k)


# perform feature re-scaling
# NOTE: only want to rescale the input features
in_features = copy.deepcopy(features_list)
in_features.pop(0)
my_dataset = rescale(my_dataset, in_features)


### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script.
### Because of the small size of the dataset, the script uses stratified
### shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html
t0 = time()

test_classifier(clf, my_dataset, features_list)

print "time:", round(time() -t0, 3), "s"

### Dump your classifier, dataset, and features_list so 
### anyone can run/check your results.

dump_classifier_and_data(clf, my_dataset, features_list)