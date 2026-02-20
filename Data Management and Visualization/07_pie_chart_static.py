import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Simple Pie Chart")

plt.show()
