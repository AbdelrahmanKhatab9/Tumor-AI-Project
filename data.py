import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


class Data:

    # Import dataset
    df = pd.read_csv('Tumor Cancer Prediction Data.csv') 
    
    # Drop index column
    df.drop("Index", axis=1, inplace=True)   # inplace -> specifies the drop operation to be in same dataframe rather creating a copy of the dataframe after drop.

     # To check if there're null values
     # print( 'Number of null values :', df.isnull().sum())
    
    # Drop rows with at least one Nan value if found
    df = df.dropna() 

    # Map strings to numbers
    df['diagnosis'] = df.diagnosis.map({"B": 0, "M": 1})
    
    # Split the data into train and test set
    x = df.iloc[:, 0:30] # Features
    y = df[['diagnosis']] # Target
    x_train, x_test, y_train, y_test = train_test_split(x , y, test_size = 0.25, random_state = 1) # 25% test  &  75% training

   # Feature Scaling - Normalizing
    stndScal = StandardScaler()  # X = ((X - X.mean()) / X.std())
    x_train = stndScal.fit_transform(x_train)
    x_test = stndScal.transform(x_test)

   # Feature Selection
    for pos, i in enumerate(df.iloc[:, 0:30]): 
          x = df[i]
          y = df["diagnosis"]
          r = x.corr(y).round(2)   
          if (abs(r)<= 0.3):
             df.drop(i, axis=1, inplace=True) # Drop F5, F10, F12, F15, F20, F23 and F25

   
    def get_head(self):
        print(self.df.head())


    def get_shape(self):
        shape = self.df.shape
        print('\nDataFrame Shape :', shape)
        print('\nNumber of rows :', shape[0])
        print('\nNumber of columns :', shape[1])

    def get_tain_test_shape(self):
        print(
                 "X train : ", self.x_train.shape,
                 "\nX test : ", self.x_test.shape,
                 "\nY train : ", self.y_train.shape,
                 "\nY test : ", self.y_test.shape
             )
    

    # Diagnosis Bar-chart
    def get_diagnosis(self):
        diagnosis_count = Counter(self.df.diagnosis)
        diagnosis_bar= pd.DataFrame.from_dict(diagnosis_count, orient='index')
        diagnosis_bar.plot(kind='bar')
        plt.show()
        

    def voting(self,model1,model2,model3,model4,model5): 
        ans = []
        for i in range(len(model1)) :
            cnt = 0
            if model1[i] == 1 :
                cnt = cnt + 1

            if model2[i] == 1 :
                cnt = cnt + 1 

            if model3[i] == 1 :
                cnt = cnt + 1 

            if model4[i] == 1 :
                cnt = cnt + 1

            if model5[i] == 1 :
                cnt = cnt + 1

            if cnt > 2 :
                ans.insert(i ,1)
            else :
                ans.insert(i,0)

        return(ans)


    # # Correlation Coefficient
    # def show_correlation(self):
    #     for pos, i in enumerate(self.df.iloc[:, 0:30]): 
    #           x = self.df[i]
    #           y = self.df["diagnosis"]
    #           r = x.corr(y).round(2)
    #           print("Correlation Between ", i, "and diagnosis : ")
    #           if abs(r) <= 0.3:
    #             print("Weak relation --> r = ",round(r, 2),"\n")
    #           elif abs(r) <= 0.6:
    #              print("Moderate relation --> r = ",round(r, 2),"\n")
    #           elif abs(r) <= 0.9:
    #              print("***************")
    #              print("Strong relation --> r = ",round(r, 2),"\n***************\n") 
    #           else:
    #              print("Perfect relation --> r = ",round(r, 2),"\n")