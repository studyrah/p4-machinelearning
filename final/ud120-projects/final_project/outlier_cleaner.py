#!/usr/bin/python


def outlierCleaner(data_dict):
    """
    simply removes the identified outliers, the outlier analysis is performed
    separately in enron_outliers.py
    """
    # we already know from the mini project we already know about total so pop
    # it out
    data_dict.pop("TOTAL",0)    
    
    # we also discovered another non person
    data_dict.pop("THE TRAVEL AGENCY IN THE PARK",0)
    
    cleaned_data = data_dict
        
    return cleaned_data

