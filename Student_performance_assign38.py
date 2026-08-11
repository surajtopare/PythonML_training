import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)



#pandas  ---  Series,                 DataFrame,             Panel
#               1D                       2D                      3D
#               Array               Multidimennsial        (removed)
#           eg one row in excel     whole sheet             all sheets in excel
#
#series consists of values
#
#


Border = "-"*50
##############################################

#step 1 Load the data set

##############################################

print(Border)
print("step 1 Load the DataSet")
print(Border)

DataPath  = "student_performance_ml.csv"

df  = pd.read_csv(DataPath) #dataframe (df)
print("data set loaded succesfully")
print("Initial entries from dataset are : ")
   
print(df.head())



##############################################
#  Step 2  : Data Analysis (EDA)
##############################################

print(Border)
print("Step 2  : Data Analysis (EDA)")
print(Border)

print("shape of dataset is : ",df.shape)  #all 

print("coloumn names  : ", list(df.columns))  #cloumn header dsiplay

print("Missing values per coloumn : ")
print(df.isnull().sum()) # total of null values

print("Class Distribution (FinalResult count) : ", df["FinalResult"].value_counts())  #names of FinalResult(labels)

print("statstical report of dataset : ", df.describe())  # whole dataset info

subset = df[df["FinalResult"] == 1]
noofpassstudent = int(len(subset))

print("No of passed students : ",noofpassstudent)

subset = df[df["FinalResult"] == 0]
nooffailedstudents = int(len(subset))

print("No of failed students : ",nooffailedstudents)

subset =   df[df["StudyHours"]]
avgstudyhrs = float(subset.aggregate())
print("abg studyhrs are : ",avgstudyhrs)


###########################################################
#  Step 3  : Decide Depenedent and Independent varaibles
###########################################################

print(Border)
print("Step 3  : Decide Depenedent and Independent varaibles")
print(Border)


# X = Independent Varaible (Features)
# Y = Depenednt Varaible (Label)


feature_cols = [
"StudyHours",
"Attendance",
"PreviousScore",
"AssignmentsCompleted",
"SleepHours"

]

X = df[feature_cols]
Y = df["FinalResult"]

print("X shape ", X.shape)
print("Y shape ", Y.shape)


###########################################################
#  Step 4  : Visualization of DataSet
###########################################################

print(Border)
print("Step 4  : Visualization of DataSet")
print(Border)

# scatter plot
plt.figure(figsize=(7,5))

for sp in df["FinalResult"].unique():
    temp = df[df["FinalResult"] == sp]
    plt.scatter(temp["StudyHours"],temp["Attendance"],label = sp)


plt.title("Student Peroformance assignement case study")

plt.xlabel("StudyHours")
plt.ylabel("Attendance")

plt.legend()
plt.grid()
plt.show()

###########################################################
#  Step 5  : Splitting  DataSet for Training and Testing
###########################################################

print(Border)
print("Step 5  : Splitting  DataSet for Training and Testing")
print(Border)


X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

print("Dataset spliting actibity done")

print("X : ", X.shape)  #(150,4)
print("Y : ",Y.shape)   #(150,)

print("X_train : ",X_train.shape) #(75,4)
print("X_test : ",X_test.shape)

print("Y_train : ",Y_train.shape) #(75,)
print("Test : ",Y_test.shape) #(75,)



###########################################################
#  Step 6  : Build the model
###########################################################

print(Border)
print(" Step 6  : Build the model")
print(Border)

model = DecisionTreeClassifier(max_depth=5)

print("Model gets created succesfully")

###########################################################
#  Step 7  : Train the model
###########################################################

print(Border)
print("Step 7  : Train the model")
print(Border)

model.fit(X_train,Y_train)

print("Model trained successfully")

###########################################################
#  Step 8  : Test  the model
###########################################################

print(Border)
print("Step 8 : Test the model")
print(Border)

Y_pred = model.predict(X_test)

print("model testing done")

print("Expected ansers : ")
print(Y_test)

print("predicated answers : ")
print(Y_pred)


###########################################################
#  Step 9  : Evaluate the model performance
###########################################################

print(Border)
print("Step 9  : Evaluate the model performance")
print(Border)

accuracy = accuracy_score(Y_test,Y_pred)
print("accuray of model is : ",accuracy*100)

print("confsuon matrix is : ")
cm = confusion_matrix(Y_test,Y_pred)

print(cm)

print("classification report : ")

print(classification_report(Y_test,Y_pred))