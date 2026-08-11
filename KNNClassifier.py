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

    #model Creation
    model = KNeighborsClassifier(n_neighbors=3)
    model = model.fit(X,Y)

    y_pred = model.predict(new_point)

    print("preicated label : ",y_pred[0])



if __name__ == "__main__":
    main()

