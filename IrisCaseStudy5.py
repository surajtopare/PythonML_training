from sklearn.datasets import load_iris




def main():
    print("-"*50)
    print("IRIS Classificsation csase study ")
    print("-"*50)

    DataSet = load_iris()

    for i in range(len(DataSet.target)):
        print("ID %d,Fetaures %s,Label %s" %(i,DataSet.data[i],DataSet.target[i]))

    

if __name__ == "__main__":
    main()