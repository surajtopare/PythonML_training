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





