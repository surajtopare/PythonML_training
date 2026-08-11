import pandas as pd

def main():
   Data = {
       "Name" : ["Sagar","Amit","Puja"],
       "Age"  : [27,28,25],
       "City" : ["Pune","Kolhapur","satara"]
 
 
       
   }
   dobj = pd.DataFrame(Data)
   print(dobj)
   
   print(dobj["Name"],["Age"])



if __name__ == "__main__":
    main()