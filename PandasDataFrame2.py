import pandas as pd

def main():
   Data = {
       "Name" : ["Sagar","Amit","Puja"],
       "Age"  : [27,28,25],
       "City" : ["Pune","Kolhapur","satara"]
 
 
       
   }
   dObj = pd.DataFrame(Data)
   print(dObj)
   #print(dObj[0])   not allowed

   print(dObj["Age"])



if __name__ == "__main__":
    main()