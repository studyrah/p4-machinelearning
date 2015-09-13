def classify(features_train, labels_train, n, lr):
    
    ### your code goes here--should return a trained ada boost classifer
    from sklearn import ensemble
        
    clf = ensemble.AdaBoostClassifier(n_estimators=n, learning_rate=lr)
    clf.fit(features_train, labels_train)
      
    return clf