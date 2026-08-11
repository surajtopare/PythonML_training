import matplotlib.pyplot as plt

# Simple line plot
x = [1, 2, 3, 4]
y = [1, 4, 2, 3]

plt.plot(x, y, marker='o', color='pink', linestyle='--')
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
