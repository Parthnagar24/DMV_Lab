import matplotlib.pyplot as plt

n = int(input("How many points? "))

x = []
y = []

for i in range(n):
    x_val = int(input(f"Enter x value for point {i+1}: "))
    y_val = int(input(f"Enter y value for point {i+1}: "))
    x.append(x_val)
    y.append(y_val)

plt.scatter(x, y, color='green')
plt.title("User Input Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()
