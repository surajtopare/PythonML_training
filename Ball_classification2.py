#Rough = 1
#smooth = 0
#Tennis = 1
#Cricket = 2

def main():
    print("ball calssifcation case study")

    # Encoding

    Features = [[35,1],[47,1],[90,0],[47,1],[90,0],[35,1],[90,0],[35,1],[35,1],[35,1],[35,1],[104,0],[90,0],[98,0],[35,0]]

    Labels = [1,1,2,1,2,1,2,1,1,1,2,2,2,2]


    print("features are : ",Features)
    print("labels are : ",Labels)

    
if __name__ == "__main__":
    main()