#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = []

    errors = (predictions - net_worths) ** 2
    cleaned_data = zip(ages, net_worths, errors)

    ### your code goes here

    def getKey(item):
        return item[2][0]

    cleaned_data.sort(key = getKey)
    
    cutoff = int(len(cleaned_data) * 0.9)
    
    cleaned_data = cleaned_data[0:cutoff]
        
    return cleaned_data

