def classify(features_train, labels_train, min_split):
    
    ### your code goes here--should return a trained decision tree classifer
    from sklearn import tree
    clf = tree.DecisionTreeClassifier(min_samples_split=min_split)
    clf.fit(features_train, labels_train)
    
    
    return clf