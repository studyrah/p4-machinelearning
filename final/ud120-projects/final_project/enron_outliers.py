#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

# seimple helper to filter the given dict by a list of 'value' criteria
# returning a tuple with the key and the value (for convenience) for each
# match
def somefiltering(filterDict, *criteria):
    #return [key for key in filterDict if all(criterion(filterDict[key]) for criterion in criteria)]
    return [(key,filterDict[key]) for key in filterDict if all(criterion(filterDict[key]) for criterion in criteria)]
    
# print the list of outliers in a nice human readable form
def prettyprintoutliers(outliers):
    for outlier in outliers:
        print "---------------------"
        print 'name: ' + outlier[0]
        for feature, value in outlier[1].iteritems():
            print feature + " : " + str(value)

# print scatter plots for each given feature against salary for the given data
# points
def visualiseFeatures(feat_list, datadict):
    
    for feature in feat_list:
        print feature
        visualiseFeature(feature, datadict)
        
# print a scatter plot for the given feature aainst salary for the given
# data points
def visualiseFeature(feat, datadict):

    features = ["poi", "salary", feat]
    data = featureFormat(datadict, features)

    for point in data:

        poi = point[0]
        salary = point[1]
        featureval = point[2]
        
        # I'm sure there are more elegant ways to conditionally colour but hey
        colour = 'blue'
        if poi == 1:
            colour = 'red'
            
        #print str(poi) + " " + str(salary) + " " + str(featureval)
        matplotlib.pyplot.scatter( salary, featureval, c=colour)
    
    matplotlib.pyplot.xlabel("salary")
    matplotlib.pyplot.ylabel(feat)
    matplotlib.pyplot.show()

### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("final_project_dataset.pkl", "r") )


"""    
#
# 1. TOTAL
#
# we already know from the mini project we already know about total - get rid
#
"""
data_dict.pop("TOTAL",0)        


features_list = [#'poi',
  'bonus',
  'deferral_payments',
  'deferred_income',
  'director_fees',
  'exercised_stock_options',
  'expenses',
  'from_messages',
  'from_poi_to_this_person',
  'from_this_person_to_poi',
  'loan_advances',
  'long_term_incentive',
  'other',
  'restricted_stock',
  'restricted_stock_deferred',
  #'salary',
  'shared_receipt_with_poi',
  'to_messages',
  'total_payments',
  'total_stock_value']


"""
#
# 2. Name check
#
# name check - are they all people and are there any accidental dupes
#
"""
names = data_dict.keys()
names.sort()
#print names
for name in names:
    print name

# ans - THE TRAVEL AGENCY IN THE PARK - get rid
data_dict.pop("THE TRAVEL AGENCY IN THE PARK",0)
   
   
"""
#
# 3. Visualise each feature
#
# plot each feature in turn against salary to spot obvious outliers
#    
"""
visualiseFeatures(features_list, data_dict)

"""
#
# 4. Having studied lets hone in on some outliers
#
"""

"""
#
# 4.1 restricted_stock_deferred
#
# one crazy outlier at 15 million when most other values are 0 (ish)
#
"""
outliers =  somefiltering(data_dict, 
                    lambda d:d['restricted_stock_deferred'] != 'NaN',
                    lambda d:d['restricted_stock_deferred'] > 1000000)

print "=================================="                    
print "Outliers - restricted_stock_deferred"                    
prettyprintoutliers(outliers)
        
# person is BHATNAGAR SANJAY (a non poi), he has big figures accross stock
# features but is it enough to remove??? Is it suspicious that
# total_payments = restricted_stock_deferred ???        
        
"""
#
# 4.1 from_messages
#
# one is emailing substantially more than others
#
"""
outliers =  somefiltering(data_dict, 
                    lambda d:d['from_messages'] != 'NaN',
                    lambda d:d['from_messages'] > 6000)

print "=================================="                    
print "Outliers - from_messages"                    
prettyprintoutliers(outliers)
        
# person is KAMINSKI WINCENTY J, nothing too alarming about other figures
# so leave in?


"""
#
# 4.2 one big poi
#
# there is one data point a poi that appears as an outlier (huge figures on
# for example loan_advances) for several features.
#
# who is it?
# if we removed this would it reveal more outliers?
#
"""
outliers =  somefiltering(data_dict, 
                    lambda d:d['loan_advances'] != 'NaN',
                    lambda d:d['loan_advances'] > 0.6e8)

print "=================================="                    
print "Outliers - loan_advances"                    
prettyprintoutliers(outliers)

# unsurprisingly LAY KENNETH L
lay = data_dict.pop("LAY KENNETH L",0)
print lay
visualiseFeatures(features_list, data_dict)

# it did reveal at least one other big financial outlier, particularly for
# features other and loan_advances but I don't think I can justify removal