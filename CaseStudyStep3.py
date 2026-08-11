import pandas as pd

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

