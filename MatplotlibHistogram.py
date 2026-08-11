import matplotlib.pyplot as plt

def main():
        marks = [44,55,60,62,65,67,70,72,75,78,80,82,85,90,92]

        plt.hist(

              marks,                            #continous data
              bins = 5,                         #no of groups
              edgecolor = "black",              #border color
              alpha = 0.8,                      #transparency
              rwidth = 0.9                      #relative width of bars


        )

        plt.title("marveloous histogram")
        plt.xlabel("Marks")
        plt.ylabel("frequcny")
        plt.show()

if __name__ == "__main__":
    main()

