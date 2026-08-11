import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def main():

    #independent

    X = np.array([
        [1,2],
        [2,3],
        [3,1],
        [5,6]]
    )
    #Depenedent

    Y = np.array(["Red","Red","Blue","Blue"])

    #testing data, to be predicted
    new_point = np.array([[3,3]])

    print("indpendnt variables are : ")
    print(X)
    print("Depenedent variables are : ")
    print(Y)
    print("testing point is : ")
    print(new_point)



if __name__ == "__main__":
    main()

