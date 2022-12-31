from data import *
from sklearn import svm
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn import metrics 
import numpy as np

class SVM: 
    
    SVM = Data()

    # Generating the model
    classifier = svm.SVC(kernel = 'linear')

    # Training the model on the Training set
    classifier.fit(SVM.x_train, SVM.y_train)

    # Predicting the test set results
    y_predict = classifier.predict(SVM.x_test)

    # Making the Confusion Matrix
    confusion_matrix = confusion_matrix(SVM.y_test, y_predict)

    # Checking the accuracy using classification_report
    c_report = classification_report(SVM.y_test, y_predict)

    # The average of the squares of the errors
    mean_square_error = metrics.mean_squared_error(np.asarray(SVM.y_test),y_predict).round(2)