from data import *
from sklearn.neighbors import KNeighborsClassifier as KNC
from sklearn.metrics import classification_report
from sklearn import metrics 
import numpy as np
from sklearn.metrics import confusion_matrix

class  KNN:

    KNN = Data()

    # Generating the model
    classifier = KNC() 
    
    # Training the model on the Training set
    classifier.fit(KNN.x_train, KNN.y_train)

    # Predicting the test set results
    y_predict = classifier.predict(KNN.x_test)

    # Making the Confusion Matrix
    confusion_matrix = confusion_matrix(KNN.y_test, y_predict)

    # Checking the accuracy using classification_report
    c_report = classification_report(KNN.y_test, y_predict)

    # The average of the squares of the errors
    mean_square_error = metrics.mean_squared_error(np.asarray(KNN.y_test),y_predict).round(2)