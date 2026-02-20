import numpy as np
import matplotlib.pyplot as plt
x=np.array([0,1,2,3,4,5,6,7])
y=np.array([0,6,11,12,20,19,30,25])
plt.figure()

plt.plot(x,y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Chart Static")
plt.show()