from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


def analysis(train, test, width):
    print('Modeling and Analysis...')

    x_train = [x[1:width + 1] for x in train] # tfidfval
    x_test = [x[1:width + 1] for x in test]
    y_train = [y[0] for y in train] # classDoc
    y_test = [y[0] for y in test]

    # Create Model by SVM
    print("Modeling by SVM")
    model = SVC(kernel='linear', random_state=None)
    model.fit(x_train, y_train)

    # Testing...
    preout = model.predict(x_test)
    print('Using test data set, Accuracy = ', accuracy_score(y_test, preout))
