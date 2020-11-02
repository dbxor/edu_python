
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
"""
speed = [32,111,138,28,59,77,97]
x = np.mean(speed)
print(x)

x = np.median(speed)
print(x)

x = stats.mode(speed)
print(x)

x = np.var(speed)
print(x)

x = np.std(speed)
print(x)

"""

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
print(np.sort(ages))
x = np.mean(ages)
print(x)

x = np.median(ages)
print(x)

x = stats.mode(ages)
print(x)

x = np.var(ages)
print(x)

x = np.std(ages)
print(x)
x = np.percentile(ages, 25)
print(x)
x = np.percentile(ages, 50)
print(x)
x = np.percentile(ages, 75)
print(x)
x = np.percentile(ages, 95)
print(x)
x = np.percentile(ages, 100)
print(x)

"""
#sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

#sns.kdeplot([0, 1, 2, 3, 4, 5])
#plt.show()

from numpy import random

x = random.normal(loc=1, scale=2, size=(2, 3))

print(x)

#sns.kdeplot(random.normal(size=1000))
#sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
#sns.kdeplot(random.binomial(n=10, p=0.5, size=1000))
sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')

plt.show()

"""