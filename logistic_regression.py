from data import *
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn import metrics 
import numpy as np
from sklearn.metrics import confusion_matrix

class  LogisticRegression:

    logistic = Data()

    # Generating the model
    classifier = LogisticRegression()

    # Training the model on the Training set
    classifier.fit(logistic.x_train, logistic.y_train.values.ravel())
    
    # Predicting the test set results
    y_predict = classifier.predict(logistic.x_test)

    # Making the Confusion Matrix
    confusion_matrix = confusion_matrix(logistic.y_test, y_predict)

    # Checking the accuracy using classification_report
    c_report = classification_report(logistic.y_test, y_predict)

    # The average of the squares of the errors
    mean_square_error = metrics.mean_squared_error(np.asarray(logistic.y_test),y_predict).round(2)