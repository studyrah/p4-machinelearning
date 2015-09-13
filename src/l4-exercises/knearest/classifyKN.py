def classify(features_train, labels_train, k):
    
    ### your code goes here--should return a trained decision tree classifer
    from sklearn import neighbors
    
    clf = neighbors.KNeighborsClassifier(n_neighbors=k)
    clf.fit(features_train, labels_train)
      
    return clf