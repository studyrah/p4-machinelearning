#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

# who is the outlier?

# well the outlier has a salary> 25 million

outlier_key = ""

for person, values in data_dict.iteritems():
    if values['salary'] > 25000000 and values['salary'] != 'NaN':
        outlier_key =  person
        print outlier_key
        print values['salary']
        
# now we have our outlier, try again

data_dict.pop(outlier_key,0)        
data = featureFormat(data_dict, features)

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

# who are the remaining outliers?

# well they have salary over 1 million

for person, values in data_dict.iteritems():
    if values['salary'] > 1000000 and values['salary'] != 'NaN':
        print person
        print values['salary']
    
    if values['bonus'] > 5000000 and values['bonus'] != 'NaN':
        print person
        print values['bonus']