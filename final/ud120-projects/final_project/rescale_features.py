# -*- coding: utf-8 -*-

"""
Get the global min and max for each feature

assumes dataset structure 'as per given code' and a list of the features
to rescale

returns dict with:
k = feature
v = (min,max)

note NaN is treated as 0
"""
def getMinsMaxs(dataset, features_to_scale):
    
    mins_maxs = {}    
    for key, features in dataset.iteritems():
        
        for feat in features_to_scale:
            
            val = features[feat]
            if val == 'NaN':
                val = 0
            
            curmin, curmax = mins_maxs.get(feat, (None, None))
                        
            if curmin == None or val < curmin:
                curmin = val

            if curmax == None or val > curmax:
                curmax = val
            
            mins_maxs[feat] = (curmin,curmax)
            
    return mins_maxs
    
"""
rescale the given features within the given dataset to be values between
0 and 1 using min / max based approach

assumes dataset structure 'as per given code' and a list of the features
to rescale

WARNING: dodgy code because as well as returning the newly scaled dataset
the original is also overwritten (sort out later)

returns dataset in the original format but with scaled features

note NaN is treated as 0
"""
    
def rescale(dataset, features_to_scale):
            
    # first we need to determine the min and max for each feature
    mins_maxs = getMinsMaxs(dataset, features_to_scale)        

    print mins_maxs    
    
    for key, features in dataset.iteritems():
                    
        for feature in features_to_scale:
            
            value = features[feature]
            #print "value is:" + str(value)
            if value == 'NaN':
                value = 0            
            
            fmin, fmax = mins_maxs[feature]

            revalue = float(value - fmin) / float(fmax - fmin)
            
            features[feature] = revalue
            
    #for person, features in dataset.iteritems():
    #    for f in features_to_scale:
    #        print person + " : " + f + " : " + str(features[f])

    return dataset            