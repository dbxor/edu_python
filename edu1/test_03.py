#%%
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

plt.style.use("ggplot")

ax.plot([10,2,113,468,51,67], color = "g")
ax.set_title("Test twinx")
ax.set_yticks([ i*100 for i in range(10)])
ax.set_xlabel("ddd")
ax.set_ylabel("ffff")

ax_2 = ax.twinx()
#ax_2.bar([20,3,66,7,80,4], color = "r", width  = 0.2)
ax_2.plot([20,3,66,7,80,4])
ax.set_yticks([ i*100 for i in range(10)])
ax_2.set_ylabel("A")

ax.legend(loc = 1)
ax_2.legend(loc = 2)
plt.show()
# %%
