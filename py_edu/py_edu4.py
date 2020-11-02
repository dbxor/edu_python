import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
numpy.random.seed(2)

# mean value is 5.0, and the standard deviation is 1.0.
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x
#print("X: %s, y: %s" %(x,y))

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 6, 100)
r2 = r2_score(test_y, mymodel(test_x))

print(r2)
plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()
