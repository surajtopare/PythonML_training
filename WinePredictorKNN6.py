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

    #step 3 : Seperate independt and dependent varaibles 
    print(border)
    print("step 3 : Seperate independt and dependent varaibles ")
    print(border)

    X = df.drop(columns=["Class"])  #dropping cloumn name class and gathering other ones all
    Y = df["Class"]
    print("shape of indpeendent variables : ",X.shape)
    print("shape of depemndent variables : ",Y.shape)

    print(border)
    print("Input cloumns : ", X.columns.tolist())
    print("Input cloumns :  Class")
    print(border)

    #step 4 :Split dataset for training and testing 
    print(border)
    print("step 4 :Split dataset for training and testing ")
    print(border)

    X_train ,X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42,stratify=Y)
    print(border)
    print("Details of training and testing data  : ")
    print("Shape of X_train : ", X_train.shape)
    print("Shape of X_train : ", X_test.shape)
    print("Shape of X_train : ", Y_train.shape)
    print("Shape of X_train : ", Y_test.shape)

    print(border)
     #step 5 :Feature scaling 
    print(border)
    print("step 5 :Feature scaling ")
    print(border)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    X_test_scaled = scaler.fit_transform(X_test)

    print("feature scaling done")
    
    print(border)
    #step 6 :Build the Model 
    print(border)
    print("step  6 :Build the Model")
    print(border)

    model = KNeighborsClassifier(n_neighbors=9)

    print("classification model is created..")

    print(border)

    #step 7 :Train the Model 
    print(border)
    print("step  7 :Train the Model")
    print(border)

    model = model.fit(X_train_scaled,Y_train)
    print("model taining completed")
    print(border)

    #step 8 :Test the Model 
    print(border)
    print("step  8 :Test the Model")
    print(border)
    Y_pred = model.predict(X_test_scaled)

    print("model testing done")

    accuracy = accuracy_score(Y_test,Y_pred)

    print("accuracy is : ", accuracy*100)

    print(border)
        
def main():
    MarvellousClassifier("WinePredictor.csv")


if __name__ == "__main__":
    main()