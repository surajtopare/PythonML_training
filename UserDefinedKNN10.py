import math
import numpy as np

def MarvellousEUCDistance(P1,P2):

    Answer = math.sqrt((P1["X"] - P2["X"])**2 + (P1["Y"] - P2["Y"])**2)
    return Answer


def MarvellousKNNClassifier(k=3):
    border = "-"*50

    Data = [
        {"point" : "A", "X" : 1, "Y" :2 ,"label" : "Red"},
        {"point" : "B", "X" : 2, "Y" :3 ,"label" : "Red"},
        {"point" : "C", "X" : 3, "Y" :1 ,"label" : "Blue"},
        {"point" : "D", "X" : 5, "Y" :6 ,"label" : "Blue"},
        {"point" : "E", "X" : 6, "Y" :6 ,"label" : "Blue"},
        {"point" : "F", "X" : 3, "Y" :4 ,"label" : "Red"},
        {"point" : "G", "X" : 3, "Y" :2 ,"label" : "Red"}

            ]

    print(border)
    print("marvellous KNN Classifier")
    new_point = {"X" : 3, "Y" : 3}
    for d in Data:
        d["distance"] = MarvellousEUCDistance(d,new_point)

    print(border)

    
    print("distances of all points:")
    print(border)
    for d in Data:
        print(d)
        
    print(border)
    soretd_data = sorted(Data,key=lambda item : item['distance'])

    print("sorted data : ")
    for d in soretd_data:
        print(d)

    print(border)

    
    nearest = soretd_data[:k]
    print(border)
    print("neartes 3 members are : ")
    print(border)
    for d in nearest:
            print(d)

    print(border)

    #voting

    votes = {}

    for neighbors in nearest:
         label = neighbors["label"]
         votes[label] = votes.get(label,0) + 1

    print(border)
    print("voting result is : ")
    print(border)

    for d in votes:
         print("Name : ",d,"number of votes : ",votes[d])

    print(border)

    iMax = 0 

    Name = ""

    for d in votes:
         if(votes[d] > iMax):
              iMax = votes[d]
              Name = d

    print("final predication is : ", Name)


 
def main():
    MarvellousKNNClassifier(5)


if __name__ == "__main__":
    main()