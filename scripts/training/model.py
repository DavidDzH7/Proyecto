
def modelo()
    clf = MLPClassifier(hidden_layer_sizes=(256,128,64,32)
                        ,activation="relu"
                        ,random_state=1).fit(X_train, y_train)

    y_pred=clf.predict(X_test)