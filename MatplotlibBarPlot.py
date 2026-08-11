import matplotlib.pyplot as plt

def main():
    language = ["C","C++","Java","Python"]
    students = [30,40,35,55]

    plt.bar(

        language,                   #values of x axis
        students,                   #values of Y axis
        width=0.6,                  #width of bars
        edgecolor = "black"  ,       #border color of bar
        linewidth = 1 ,             # width of bar border
        alpha = 0.8,                #transparcny 0.0  to 1.0
        label = "Students"          #legend text


    )
    plt.title("marvellous bar plot")
    plt.xlabel("Languagaes")
    plt.ylabel("no of students")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()

