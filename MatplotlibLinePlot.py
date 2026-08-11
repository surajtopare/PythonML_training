import matplotlib.pyplot as plt

def main():
    X = [1,2,3,4,5]
    Y = [10,25,18,35,30]

    plt.plot(
        X,                          #values of X axix
        Y,
        marker = "o",               #symbol to dislay marker
        linestyle = "--",
        linewidth = 2,
        markersize = 7,
        label = "Marks"
    )
    plt.title("marvellous title plot")
    plt.xlabel("student number")
    plt.ylabel("Student marks")

    plt.grid(True)  #boxes  behind
    plt.legend() #display
    plt.show() #digram from RAM to h/w

if __name__ == "__main__":
    main()

