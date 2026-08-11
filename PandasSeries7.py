import pandas as pd
#every series is a list (series from pandas library)
#vice versa is not true , every list is not series
def main():
   sobj = pd.Series([27000,32000,35000],index = ["Amit","Sagar","Puja"])
   print(sobj)
   print(sobj["Sagar"])


if __name__ == "__main__":
    main()