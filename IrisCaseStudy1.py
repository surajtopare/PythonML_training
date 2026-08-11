from sklearn.datasets import load_iris




def main():
    print("-"*50)
    print("IRIS Classificsation csase study ")
    print("-"*50)

    DataSet = load_iris()
    print(DataSet)


if __name__ == "__main__":
    main()