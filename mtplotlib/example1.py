# Comment like a pro.
import matplotlib.pyplot as plt
import math
# Graph the function y =  3x3 - 2x2 + 4x - 1
x_axis = []
y_axis = []
for x in range(-100, 101):
    y = 3 * x ** 3 - 2* x ** 2 + 4 * x - 1
    x_axis.append(x)
    y_axis.append(y)
plt.plot(x_axis, y_axis)
plt.xlabel('Domain Values (x)')
plt.ylabel('Range Values (y)')
plt.title('Graph of y =  3x3 - 2x2 + 4x - 1')
plt.grid(True)
plt.show()