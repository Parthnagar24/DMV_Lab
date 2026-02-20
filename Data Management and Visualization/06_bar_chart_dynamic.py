import matplotlib.pyplot as plt

names = ['A', 'B', 'C', 'D']


values = []
for name in names:
    val = int(input(f"Enter value for {name}: "))
    values.append(val)

plt.bar(names, values, color='orange')
plt.ylim(0, max(values) + 5)
plt.title("Dynamic Bar Chart")

plt.show()
