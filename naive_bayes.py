from data import *
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report
from sklearn import metrics 
import numpy as np

class  NaiveBayes:

    naive = Data()

    # Generating the model
    classifier = GaussianNB()
    
    # Training the model on the Training set
    classifier.fit(naive.x_train, naive.y_train.values.ravel()) # ravel --> Returns 1D array

    # Predicting the test set results
    y_predict = classifier.predict(naive.x_test)

    # Making the Confusion Matrix
    confusion_matrix = confusion_matrix(naive.y_test, y_predict)

    # Checking the accuracy using classification_report
    c_report = classification_report(naive.y_test, y_predict)

    # The average of the squares of the errors
    mean_square_error = metrics.mean_squared_error(np.asarray(naive.y_test),y_predict).round(2)