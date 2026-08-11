from sklearn.datasets import load_iris




def main():
    print("-"*50)
    print("IRIS Classificsation csase study ")
    print("-"*50)

    DataSet = load_iris()
    #metadata of dataset
    print("Indpenednt varoabels are : ")
    print(DataSet.feature_names)

    print("Dependnt varoabels are : ")
    print(DataSet.target_names)




if __name__ == "__main__":
    main()