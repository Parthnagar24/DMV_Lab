import matplotlib.pyplot as plt
import numpy as np
import time

plt.ion()  

x = np.linspace(0, 10, 100)
fig, ax = plt.subplots()

for i in range(1, 11):
    y = np.sin(x + i/2)
    ax.clear()  
    ax.plot(x, y)
    ax.set_title(f"Dynamic Sine Wave Step {i}")
    plt.pause(0.5)  

plt.ioff() 
plt.show()
