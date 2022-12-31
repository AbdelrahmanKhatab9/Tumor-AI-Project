from data import *
import numpy as np
from sklearn.tree import DecisionTreeClassifier 
from sklearn import metrics 
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

class ID3:

    id3 = Data()

    # Generating the model
    classifier = DecisionTreeClassifier(criterion = 'entropy', max_depth = 5, random_state = 1)

    # Training the model on the Training set
    classifier = classifier.fit(id3.x_train,id3.y_train)

    # Predicting the test set results
    y_predict = classifier.predict(id3.x_test)

    # Making the Confusion Matrix
    confusion_matrix = confusion_matrix(id3.y_test, y_predict)

    # Checking the accuracy using classification_report
    c_report = classification_report(id3.y_test, y_predict)

    # The average of the squares of the errors
    mean_square_error = metrics.mean_squared_error(np.asarray(id3.y_test),y_predict).round(2)