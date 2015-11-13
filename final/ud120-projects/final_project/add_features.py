#!/usr/bin/python
from rescale_features import rescale
from copy import deepcopy

def addFeatures(data_dict, features_list):
    """

    """

    # we don't want to inadvertently change the data_dict
    # just yet so take a copy of data_dict so we can play
    # with some of the features
    # (yes it is wasteful to copy the whole thing)
    data_dict_copy = deepcopy(data_dict)
    
    # now we must will rescale the features so that we
    # have a level playing field
    #(technically unecessary with these choices as they
    # are of similar scale)
    data_dict_rescale = rescale(data_dict_copy, ['from_poi_to_this_person', 
                             'from_this_person_to_poi',
                             'shared_receipt_with_poi'])
     
    #data_dict_rescale = data_dict_copy                        
    # now create the new feature
    cnt = 0
    for person, features in data_dict_rescale.iteritems():
        
        frompoi = features['from_poi_to_this_person']
        frompoi = 0 if frompoi == 'NaN' else frompoi        
        
        topoi = features['from_this_person_to_poi']
        topoi = 0 if topoi == 'NaN' else topoi

        sharedpoi = features['shared_receipt_with_poi']
        sharedpoi = 0 if sharedpoi == 'NaN' else sharedpoi
        
        #print str(frompoi) + " : " + str(topoi) + " : " + str(sharedpoi)
        shared_messages = frompoi + topoi + sharedpoi
        
        # now add to data_dict
        data_dict[person]['shared_messages'] = shared_messages
        cnt += 1
        
    print "data_dict size: " + str(len(data_dict))
    print "cnt: " + str(cnt)
    features_list.append('shared_messages')
    return (data_dict, features_list)