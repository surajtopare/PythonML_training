import math
import numpy as np

def MarvellousEUCDistance(P1,P2):

    Answer = math.sqrt((P1["X"] - P2["X"])**2 +(P1["Y"] - P2["Y"])**2)
    return Answer


def MarvellousKNNClassifier():
    border = "-"*50

    Data = [
        {"point" : "A", "X" : 1, "Y" :2 ,"label" : "Red"},
        {"point" : "B", "X" : 2, "Y" :3 ,"label" : "Red"},
        {"point" : "C", "X" : 3, "Y" :1 ,"label" : "Blue"},
        {"point" : "D", "X" : 5, "Y" :6 ,"label" : "Blue"}

            ]

    print(border)
    print("marvellous KNN Classifier")

    for i in Data:
        print(i)

    print(border)

    new_point = {"X" : 3, "Y" : 3}

    Result = MarvellousEUCDistance(Data[0],new_point)
    print("distance is :  ",Result)

def main():
    MarvellousKNNClassifier()


if __name__ == "__main__":
    main()