import matplotlib.pyplot as plt

def main():
    studyhrs = [1,2,3,4,5,6]
    marks = [35,42,50,62,72,85]

    plt.scatter(

        studyhrs,
        marks,
        s = 100,
        marker="o",
        alpha=0.8,
        edgecolors="black",
        linewidths=1,
        label="Students"
    )

    plt.title("marvellous scatter plot")
    plt.xlabel("Study Hrs")
    plt.ylabel("MArks")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

