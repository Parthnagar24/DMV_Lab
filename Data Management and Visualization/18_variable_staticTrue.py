import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y=[10,20,15,25,30]

plt.plot(x,y,marker='o')

plt.xlabel("X values (Independent variable)")
plt.ylabel("Y values (Dependent variable)")

plt.title("X-Y axis data plot")

plt.grid(True)
plt.show()




import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,15,25,30]

plt.figure()

line, = plt.plot(x, y, marker='o')

plt.xlabel("X values (Independent variable)")
plt.ylabel("Y values (Dependent variable)")
plt.title("X-Y axis data plot")
plt.grid(True)


new_x = [1,2,3,4,5,6]
new_y = [10,20,15,25,30,35]

line.set_xdata(new_x)
line.set_ydata(new_y)

plt.xlim(min(new_x), max(new_x))
plt.ylim(min(new_y), max(new_y))

plt.draw()
plt.show()
