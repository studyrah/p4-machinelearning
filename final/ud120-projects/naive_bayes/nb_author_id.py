#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 1 (Naive Bayes) mini-project 

    use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
#rahaugh - had to create the tools and data (maildir) data dirs under my
#project as their code assumes a certain path all over the place
sys.path.append("../tools")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
#test

#########################################################


### import the sklearn module for GaussianNB
from sklearn.naive_bayes import GaussianNB

### create classifier   
clf = GaussianNB()

### fit the classifier on the training features and labels
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time() -t0, 3), "s"
    
### use the trained classifier to predict labels for the test features
t0 = time()
pred = clf.predict(features_test)
print "predicting time:", round(time() -t0, 3), "s"

### calculate and return the accuracy on the test data
### this is slightly different than the example, 
### where we just print the accuracy
### you might need to import an sklearn module

### alternatively
#from sklearn.metrics import accuracy_score
#print accuracy_score(features_test, labels_test)
    
accuracy = clf.score(features_test, labels_test)

print(pred)
print(accuracy)


