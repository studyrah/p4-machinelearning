#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors
    
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

from class_vis import prettyPicture



### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
#clf = SVC(kernel="linear")


# (rahaugh) sample training set to 1%
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100]


#c_values = [1,10,100,1000,10000]
c_values = [10000]


for c in c_values:

    clf = SVC(kernel="rbf", C=c)


    #### now your job is to fit the classifier
    #### using the training features/labels, and to
    #### make a set of predictions on the test data
    
    print "about to fit: c = " + str(c)
    t0 = time()
        
    clf.fit(features_train, labels_train)
    print "training time:", round(time() -t0, 3), "s"
    
    #### store your predictions in a list named pred
    pred = clf.predict(features_test)
    
    print "10: " + str(pred[10])
    print "26: " + str(pred[26])
    print "50: " + str(pred[50])    
    
    print "Chris: " + str(len(pred[pred == 1]))
    print "Sara: " + str(len(pred[pred == 0]))
    
    from sklearn.metrics import accuracy_score
    
    t0 = time()
    acc = accuracy_score(pred, labels_test)
    print "predicting time:", round(time() -t0, 3), "s"
    
    print acc
    
    #prettyPicture(clf, features_test, labels_test)



def submitAccuracy():
    return acc
    

if __name__ == "__main__":
    print(submitAccuracy())    
#########################################################


