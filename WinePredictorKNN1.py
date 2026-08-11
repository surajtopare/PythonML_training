import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler



def MarvellousClassifier(DataPath):
    border = "-"*60

    print(border)
    print("Step 1 : Load the data set from CSV file")
    print(border)

    df = pd.read_csv(DataPath)

    print(border)
    print("some entries from dataset : ")
    print(df.head())

    print(border)

    
def main():
    MarvellousClassifier("WinePredictor.csv")


if __name__ == "__main__":
    main()