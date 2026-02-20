import numpy as np
import matplotlib.pyplot as plt
data=np.array([1,2,2,2,3,3,4,4,5,6,7,7,7,7])

plt.figure()
plt.hist(data)

plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Static histogram")
plt.show()