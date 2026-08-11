import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier



#pandas  ---  Series,                 DataFrame,             Panel
#               1D                       2D                      3D
#               Array               Multidimennsial        (removed)
#           eg one row in excel     whole sheet             all sheets in excel
#
#


Border = "-"*50
##############################################

#step 1 Load the data set

##############################################

print(Border)
print("step 1 Load the DataSet")
print(Border)

DataPath  = "iris.csv"

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

print("Class Distribution (species count) : ", df["species"].value_counts())  #names of species(labels)

print("statstical report of dataset : ", df.describe())  # whole dataset info

###########################################################
#  Step 3  : Decide Depenedent and Independent varaibles
###########################################################

print(Border)
print("Step 3  : Decide Depenedent and Independent varaibles")
print(Border)


# X = Independent Varaible (Features)
# Y = Depenednt Varaible (Label)


feature_cols = [
"sepal length (cm)",
"sepal width (cm)",
"petal length (cm)",
"petal width (cm)"
]

X = df[feature_cols]
Y = df["species"]

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

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"],temp["petal width (cm)"],label = sp)


plt.title("Marvellous IRIS case study")

plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

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