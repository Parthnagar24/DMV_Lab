import matplotlib.pyplot as plt


names = ['A', 'B', 'C', 'D']
values = [10, 25, 15, 30]


plt.bar(names, values, color='skyblue')

plt.title("Static Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")

plt.show()