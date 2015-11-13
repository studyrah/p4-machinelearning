def classify(features_train, labels_train, n, mss):
    
    ### your code goes here--should return a trained random forest classifer
    from sklearn import ensemble
        
    clf = ensemble.RandomForestClassifier(n_estimators = n, min_samples_split = mss)
    clf.fit(features_train, labels_train)
      
    return clf