#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import sys

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#print enron_data["SKILLING JEFFREY K"]

#Q. how many people are int the dataset?
print "numpeople: " + str(len(enron_data))
# 146

#For each person, how many features are available?
maxfeatures = 0
for person in enron_data.keys():
    features = enron_data[person].keys()
    
    if len(features) > maxfeatures:
        maxfeatures = len(features)

print "maxfeatures: " + str(maxfeatures)
# 21



#How many POI's are there in the data set?
numpoi = 0
for person in enron_data.keys():
    if enron_data[person]['poi'] == True:
        numpoi += 1

print "numpoi: " + str(numpoi)
# 18


# how many poi's were ther in total?
#in a separate file

actualnumpoi = 0
with open('../final_project/poi_names.txt', 'r') as f:

    #skip over two pre lines
    f.readline()
    f.readline()
    
    for line in f:
        actualnumpoi += 1
        #if line.startswith('(y)'):
        #    actualnumpoi += 1

print "actualnumpoi: " + str(actualnumpoi)
# 35

# What is the total value of stock belonging to James Prentice?
print "James Prentice total stock value: " + str(enron_data['PRENTICE JAMES']['total_stock_value'])
# $1095040

# How many email messages do we have from Wesley Colwell to persons of interest

print "num messages from WC to POI: " + str(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])
# 11


# What's the value of stock options exercised by Jeffrey Skilling?

print "value of stock options exerciese for JS: " + str(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])
# 19250000

#Of these three individuals (Lay, Skilling and Fastow), who took home the most money (largest value of "total_payments" feature)? 
#(Lay, Fastow, Skilling)

asf = enron_data['FASTOW ANDREW S']['total_payments']
jks = enron_data['SKILLING JEFFREY K']['total_payments']
kll = enron_data['LAY KENNETH L']['total_payments']

print "asf: " + str(asf)
print "jks: " + str(jks)
print "kll: " + str(kll)
#Lay


#How much money did that person get?
# 103559793


# How many people have a quantified salary?
# How many people have a known email address?
numquantifiedsalary = 0
numknownemailaddress = 0
for person in enron_data.keys():
    if enron_data[person]['salary'] != 'NaN':
        numquantifiedsalary += 1
        
    if enron_data[person]['email_address'] != 'NaN':
        numknownemailaddress += 1

print "numquantifiedsalary: " + str(numquantifiedsalary)
print "numknownemailaddress: " + str(numknownemailaddress)
# 95
# 111

sys.path.append("../tools")
from feature_format import featureFormat
from feature_format import targetFeatureSplit


feature_list = ["poi", "salary", "bonus"] 
data_array = featureFormat( enron_data, feature_list )
label, features = targetFeatureSplit(data_array)

#print data_array
print label
#print features

