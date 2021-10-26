from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


def analysis(train, test, width):
    x_train = [x[1:width + 1] for x in train] # tfidfval
    x_test = [x[1:width + 1] for x in test]
    y_train = [y[0] for y in train] # classDoc
    y_test = [y[0] for y in test]

    # Create Model by SVM
    model = SVC(kernel='linear', random_state=None)
    model.fit(x_train, y_train)

    # Testing...
    preout = model.predict(x_test)
    print('Using test data set, Accuracy = ', accuracy_score(y_test, preout))

    mat = confusion_matrix(y_test, preout)
    print('confusion matrix')
    print(mat)
    print('precision', mat[0][0]/(mat[0][0]+mat[1][0]))
    print('recallate', mat[0][0]/(mat[0][0]+mat[0][1]))
