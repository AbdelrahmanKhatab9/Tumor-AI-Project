from data import *
from id3 import *
from knn import *
from logistic_regression import *
from naive_bayes import *
from svm import *

from PIL import Image, ImageTk
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import customtkinter

df = Data()


global ls
ls = []

count = 0

filename =""

pred_model1 = [] 
pred_model2 = []
pred_model3 = []
pred_model4 = [] 
pred_model5 = []
predict_vote = []

def browseFiles():
    global filename 
    global pred_model1 
    global pred_model2
    global pred_model3 
    global pred_model4 
    global pred_model5   
    global predict_vote
    global count 
    count = 0

    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("csv files",
                                                        "*.csv*"),
                                                       ("all files",
                                                        "*.*")))    
    data = pd.read_csv(filename)
    
    data = data.dropna() # drop rows with at least one Nan value
    data = data.drop_duplicates(inplace = False) # drop dulicates values

    data.drop("Index", axis=1, inplace=True)
   
    x = data.iloc[:, 0:30]
    
    # Feature Scaling - Normalizing
    x = df.stndScal.transform(x)
   
    pred_model1 = model1.classifier.predict(x)
    pred_model2 = model2.classifier.predict(x) 
    pred_model3 = model3.classifier.predict(x)  
    pred_model4 = model4.classifier.predict(x) 
    pred_model5 = model5.classifier.predict(x) 
    predict_vote = df.voting(pred_model1,pred_model2,pred_model3,pred_model4,pred_model5)
    
    print("SVM Predction : ", pred_model1)  
    print("Logistic Regression Predction : ", pred_model2)  
    print("ID3 Predction : ", pred_model3)  
    print("Naive Bayes Predction : ",pred_model4)  
    print("KNN Predction : ", pred_model4)  
    print ("Vote Prediction :", predict_vote)
    
    ls.clear()
    
    for i in range(len(predict_vote)):
        if predict_vote[i]==0:
            ls.append("Benign")
        else:
            ls.append("Malignant")
        
    ls[count]        

    # Change label contents
    app.label_info_1.configure(text="Row Number : "+str(count )+ "\nVoting Prediction : "+ls[count])
    print("Row Number :"+str(count )+ "\nPrediction : "+ls[count])

bool_Voting = False
bool_svm = False
bool_nav = False
bool_knn = False
bool_logic = False
bool_id = False   
    
# Voting GUI 
def Voting_Display():
    global bool_Voting
    global bool_svm 
    global bool_nav
    global bool_knn
    global bool_logic
    global bool_id
    bool_Voting = True
    bool_svm = False
    bool_nav = False
    bool_knn = False
    bool_logic = False
    bool_id = False
   
    ls.clear()

    for i in range(len(predict_vote)):
       if predict_vote[i] == 0:
           ls.append("Benign")
       else:
           ls.append("Malignant")
    app.label_info_1.configure(text="Row Number : "+str(count )+"\nVoting Prediction : "+ls[count])

# SVM GUI
def SVM_Display():
    global bool_Voting
    global bool_svm 
    global bool_nav
    global bool_knn
    global bool_logic
    global bool_id
    bool_Voting = False
    bool_svm = True
    bool_nav = False
    bool_knn = False
    bool_logic = False
    bool_id = False
    
    ls.clear()
    for i in range(len(pred_model1)):
        if pred_model1[i]==0:
            ls.append("Benign")
        else:
            ls.append("Malignant")
    app.label_info_1.configure(text="Row Number : "+str(count )+"\nSVM Prediction: "+ls[count])

# Logistic GUI
def lods_Display():
    global bool_Voting
    global bool_svm 
    global bool_nav
    global bool_knn
    global bool_logic
    global bool_id
    bool_Voting = False
    bool_svm = False
    bool_nav = False
    bool_knn = False
    bool_logic = True
    bool_id = False
    ls.clear()
    for i in range(len(pred_model2)):
        if pred_model2[i]==0:
            ls.append("Benign")
        else:
            ls.append("Malignant")
    app.label_info_1.configure(text="Row Number : "+str(count )+"\nLogistic Prediction : "+ls[count])
   
# ID3 GUI 
def Id3_Display():
    global bool_Voting
    global bool_svm 
    global bool_nav
    global bool_knn
    global bool_logic
    global bool_id
    bool_Voting = False
    bool_svm = False
    bool_nav = False
    bool_knn = False
    bool_logic = False
    bool_id = True
    
    ls.clear()
    for i in range(len(pred_model3)):
        if pred_model3[i]==0:
           ls.append("Benign")
        else:
           ls.append("Malignant")
    app.label_info_1.configure(text="Row Number : "+str(count )+"\nID3 Prediction : "+ls[count])  

# Naive GUI
def Nav_Display():
    global bool_Voting
    global bool_svm 
    global bool_nav
    global bool_knn
    global bool_logic
    global bool_id
    bool_Voting = False
    bool_svm = False
    bool_nav = True
    bool_knn = False
    bool_logic = False
    bool_id = False
    
    ls.clear()
    for i in range(len(pred_model4)):
        if pred_model4[i]==0:
            ls.append("Benign")
        else:
            ls.append("Malignant")
    app.label_info_1.configure(text="Row Number : "+str(count )+"\nNaive-Bayes Prediction : "+ls[count])

# KNN GUI
def Knn_Display():
    global bool_Voting
    global bool_svm 
    global bool_nav
    global bool_knn
    global bool_logic
    global bool_id
    bool_Voting = False
    bool_svm = False
    bool_nav = False
    bool_knn = True
    bool_logic = False
    bool_id = False
    
    ls.clear()
    
    for i in range(len(pred_model5)):
        if pred_model5[i]==0:
            ls.append("Benign")
        else:
            ls.append("Malignant")
    app.label_info_1.configure(text= "Row Number : "+str(count )+"\nKNN Prediction : "+ls[count])
    
def Next_Step():
    global bool_Voting
    global bool_svm 
    global bool_nav
    global bool_knn
    global bool_logic
    global bool_id
    global count

    if count < len(ls):
       count=count+1
       print("Row Number :"+str(count )+ "\nPrediction : "+ls[count])
       model="Voting Prediction :  "
       if bool_Voting == True:
           model = "Voting Prediction : "
       if bool_svm == True:
           model="SVM Prediction : "
           
       if bool_id == True:
           model="ID3 Prediction : "    
       
       if bool_knn == True:
            model="KNN Prediction : "   
       
       if bool_logic == True:
           model="Logistic Prediction : "
           
       if bool_nav == True:
           model="Naive-Bayes Prediction : "    
           
       app.label_info_1.configure( text= "Row Number : "+str(count )+ '\n'+ model+ls[count])
    else:
        print("Error","Data is finshed!!")
        
def Back_Step():
    global count
    if count >= 0:
      count=count-1
      print("Row Number :"+str(count )+ "\nPrediction : "+ls[count])
      model="Voting Prediction :  "
      if bool_Voting == True:
          model = "Voting Prediction : "
      if bool_svm == True:
          model="SVM Prediction : "
          
      if bool_id == True:
          model="ID3 Prediction : "    
      
      if bool_knn == True:
           model="KNN Prediction : "   
      
      if bool_logic == True:
          model="Logistic Prediction : "
          
      if bool_nav == True:
          model="Naive-Bayes Prediction : "    
      app.label_info_1.configure(text="Row Number : "+str(count ) + '\n'+ model+ls[count])
    else:
        print("Error","Data is finshed!!")
                                                                                                                      
# Create the root window
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):

    WIDTH = 880
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("TumorCancerPrediction")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(9, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="TumorCancerPrediction",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Voting",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=Voting_Display)
        self.button_1.grid(row=2, column=0, pady=20, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="SVM",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=SVM_Display)
        self.button_2.grid(row=3, column=0, pady=20, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Naive-Bayes",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=Nav_Display)
        self.button_3.grid(row=4, column=0, pady=20, padx=20)
        
        self.button_4 = customtkinter.CTkButton(master=self.frame_left,
                                                text="ID3",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=Id3_Display)
        self.button_4.grid(row=5, column=0, pady=20, padx=20)
        
        
        self.button_5 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Logistic",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=lods_Display)
        self.button_5.grid(row=6, column=0, pady=20, padx=20)
        
        self.button_6 = customtkinter.CTkButton(master=self.frame_left,
                                                text="KNN",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=Knn_Display)
        self.button_6.grid(row=7, column=0, pady=20, padx=20)




     

        self.switch_2 = customtkinter.CTkSwitch(master=self.frame_left,
                                                text="Dark Mode",
                                                command=self.change_mode)
        self.switch_2.grid(row=10, column=0, pady=5, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=10)
        self.frame_info.columnconfigure(0, weight=10)
    
        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="Welcome",
                                                   height=300,width=100,
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=10, sticky="nwe", padx=15, pady=15)
     
        self.button_500 = customtkinter.CTkButton(master=self.frame_right ,
                                         text="Back",
                                         command=Back_Step)
        self.button_500.grid(row=2 ,column=2, columnspan=2, ipady=10, padx=30, sticky="we")
        self.button_501 = customtkinter.CTkButton(master=self.frame_right,
                                         text="Next",  
                                         command=Next_Step)
        self.button_501.grid(row=1, column=2, columnspan=2, ipady=10, padx=30, sticky="we")

        # ============ frame_right ============

        self.button_50 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Upload File", 
                                                command=browseFiles)
        self.button_50.grid(row=5, column=0, columnspan=2, ipady=15, padx=120, sticky="we")

        # set default values
       
        self.switch_2.select()
         
    
    def button_event(self):
        print("Button Pressed")

    def change_mode(self):
        if self.switch_2.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def on_closing(self, event=0):
        self.destroy()

df.get_shape()
print("________________________________________________________________________________________")

df.get_head()
print("________________________________________________________________________________________")

#df.get_diagnosis()

df.get_tain_test_shape()
print("________________________________________________________________________________________")

model1 = SVM()
print('**SVM Confusion Matrix : **', model1.confusion_matrix, sep='\n')
print('**SVM Report : **', model1.c_report, sep='\n')
print('**SVM Mean Suqare Error:**', model1.mean_square_error, sep='\n')
print("________________________________________________________________________________________")

model2 = LogisticRegression()
print('**Logistic Regression Confusion Matrix : **', model2.confusion_matrix, sep='\n')
print('**Logistic Regression Report : **', model2.c_report, sep='\n')
print('**Logistic Mean Suqare Error:**', model2.mean_square_error, sep='\n')
print("________________________________________________________________________________________")

model3 = ID3()
print('**ID3 Confusion Matrix : **', model3.confusion_matrix, sep='\n')
print('**ID3 Report : **', model3.c_report, sep='\n')
print('**ID3 Mean Suqare Error:**', model3.mean_square_error, sep='\n')
print("________________________________________________________________________________________")

model4 = NaiveBayes()
print('**Naive Bayes Confusion Matrix : **', model4.confusion_matrix, sep='\n')
print('**Naive Bayes Report : **', model4.c_report, sep='\n')
print('**Naive Mean Suqare Error:**', model4.mean_square_error, sep='\n')
print("________________________________________________________________________________________")

model5 = KNN()
print('**KNN Confusion Matrix : **', model5.confusion_matrix, sep='\n')
print('**KNN Report : **', model5.c_report, sep='\n')
print('**KNN Mean Suqare Error:**', model5.mean_square_error, sep='\n')
print("________________________________________________________________________________________")

predict_y = df.voting(model1.y_predict,model2.y_predict,model3.y_predict,model4.y_predict,model5.y_predict)
print ("Voting Prediction :",predict_y)

if __name__ == "__main__":
    app = App()
    app.resizable(width=False, height=False)
    app.mainloop()