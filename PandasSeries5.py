import pandas as pd
#every series is a list (series from pandas library)
#vice versa is not true
def main():
   sobj = pd.Series([11,21,51,101],index = [5,6,7,8])
   print(sobj)
   print(sobj[7])


if __name__ == "__main__":
    main()