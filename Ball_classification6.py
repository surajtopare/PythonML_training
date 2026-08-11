from sklearn import tree

def main():
    print("ball calssifcation case study")

   

    Independent = [[35,1],[47,1],[90,0],[47,1],[90,0],[35,1],[90,0],[35,1],[35,1],[35,1],[35,1],[104,0],[90,0]]

    Dependent = [1,1,2,1,2,1,2,1,1,1,1,2,2]

    #testing  independt [35,1],[90,0]  
    #testing dependent [1,2]

    model = tree.DecisionTreeClassifier()
    model = model.fit(Independent,Dependent) #training

    Result = model.predict([[35,1],[90,0]])

    print("predciated result of model is : ",Result)

    
if __name__ == "__main__":
    main()