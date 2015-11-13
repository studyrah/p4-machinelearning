#!/usr/bin/python
import os
from poi_identifiers import poiIdentifiers
import sys
sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

emails_by_address_path = './emails_by_address'

"""
adds a new feature which is simply a count of how many emails a poi was referred
to in the body of emails sent by a given person.

where a reference means either email address listed or both first and surname
"""
def addFeatures(data_dict, features_list):

    emaillistings = os.listdir(emails_by_address_path)

    for person, features in data_dict.iteritems():

        mentions = 0
        
        eaddr = features['email_address']
        
        listing = "from_" + eaddr + ".txt"
                
        if listing in emaillistings:

            emailfiles = open(emails_by_address_path + '/' + listing, 'r')
            
            for emailfilepath in emailfiles:
                #emailfilepath = emailfilepath.replace('enron_mail_20110402/','../')
                
                email = open(emailfilepath.strip())
                
                words = parseOutText(email)
                                
                # contains email address or names
                mentions += num_mentions(words, poiIdentifiers(), person)
            
        print person + " : " + str(mentions)
        
        features['mentions'] = mentions
        
    features_list.append('mentions')                
    
    return (data_dict, features_list)    
    

"""
Returns a count of mentions of names or emails in the wordlist
where:

wordlist - simply the corpus of words to search in
checkdict - dict keyed by the poi fullname and containing poi first/surnames
            and emails

increments mention if both first and surname appear in the wordlist
increments mention if any of the emails appear in the wordlist
"""
def num_mentions(wordlist, checkdict, person):
    mentions = 0
    
    for checkperson, checklists in checkdict.iteritems():
        if person != checkperson:
            names = checklists['names']

            # if we see both first and surname add a mention
            if all(name.lower() in wordlist for name in names):
                mentions += 1
                
            emails = checklists['emails']
                
            # if we see any of the emails add a mention
            if any(email.lower() in wordlist for email in emails):
                mentions += 1
    
    return mentions
    
def main():
    
    import sys
    import pickle

    sys.path.append("../tools/")

    features_filename = './features_v4.txt'
    features_list = [line.rstrip('\n') for line in open(features_filename)]  

    ### Load the dictionary containing the dataset
    data_dict = pickle.load(open("final_project_dataset.pkl", "r") )

    data_dict, features_list = addFeatures(data_dict, features_list)
    
    pickle.dump(data_dict, open("final_project_dataset_modified.pkl", "w") )
    pickle.dump(features_list, open("final_project_features_list_modified.pkl", "w") )

    data_dict = pickle.load(open("final_project_dataset_modified.pkl", "r") )
    features_list = pickle.load(open("final_project_features_list_modified.pkl", "r") )    

    print "=================================================================="    
    print features_list
    print "=================================================================="    
    print data_dict            
    
if __name__ == '__main__':
    main()
