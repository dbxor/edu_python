
import numpy as np
import matplotlib.pyplot as plt 

x = np.arange(-1,2,0.1)
y = x**2 + 2*x + 3

plt.plot(x,y)
plt.show()