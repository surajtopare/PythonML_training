import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler



def MarvellousClassifier(DataPath):
    border = "-"*60

    #step 1 : Load the data set from CSV file
    print(border)
    print("Step 1 : Load the data set from CSV file")
    print(border)

    df = pd.read_csv(DataPath)

    print(border)
    print("some entries from dataset : ")
    print(df.head())

    print(border)

    #step 2 : clean the  the data set 
    print(border)
    print("Step 2 : Clean the  the data set")
    print(border)

    df.dropna(inplace=True) #remove missing values(Nan,None,NaT)  #inplace true -- in that file only original dataset
    print("shape of dataset is : ",df.shape)
    print("total records : ", df.shape[0])
    print("total cloumns : ", df.shape[1])
    print(border)

    


    
def main():
    MarvellousClassifier("WinePredictor.csv")


if __name__ == "__main__":
    main()