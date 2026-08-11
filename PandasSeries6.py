import pandas as pd
#every series is a list (series from pandas library)
#vice versa is not true , every list is not series
def main():
   sobj = pd.Series([11,21,51,101],index = ["C","C++","Java","Python"])
   print(sobj)
   print(sobj["Python"])


if __name__ == "__main__":
    main()