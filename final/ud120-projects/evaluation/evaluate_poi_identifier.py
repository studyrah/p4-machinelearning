#!/usr/bin/python


"""
    starter code for the evaluation mini-project
    start by copying your trained/tested POI identifier from
    that you built in the validation mini-project

    the second step toward building your POI identifier!

    start by loading/formatting the data

"""
import numpy
import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 

from sklearn import cross_validation

# split into test and train set
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(
     features, labels, test_size=0.3, random_state=42)

from sklearn.tree import DecisionTreeClassifier

#clf = DecisionTreeClassifier(min_samples_split=40)
clf = DecisionTreeClassifier()

clf.fit(features_train, labels_train)

#t0 = time()
#print "predicting time:", round(time() -t0, 3), "s"
pred = clf.predict(features_test)


from sklearn.metrics import accuracy_score    

acc = accuracy_score(pred, labels_test)

print acc

#Q. How many POI are predicted in the test set?
print pred.sum() # 4

#Q. How many people total are in the test set?
print len(pred) # 29

#Q. If your predictor predicted 0 POI what would its accuracy be?

acc0 = accuracy_score(numpy.zeros(29), labels_test)
print acc0

#Q. Do we get any true positives?
truepos = (labels_test == 1) and (pred == labels_test)
print truepos

truepos = (labels_test == 1) & (labels_test == pred)
print truepos.sum()

#Q what is the precision and recall
from sklearn.metrics import precision_score

prec = precision_score(labels_test, pred)
print prec

from sklearn.metrics import recall_score

rec = recall_score(labels_test, pred)
print rec






#predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
#true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

#print precision_score(true_labels, predictions)
#print recall_score(true_labels, predictions)