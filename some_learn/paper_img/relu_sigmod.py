import math
import numpy as np
import matplotlib.pyplot as plt

# set x's range
x = np.arange(-10, 10, 0.1)

y1 = 1 / (1 + math.e ** (-x))  # sigmoid
# y2=math.e**(-x)/((1+math.e**(-x))**2)
y2 = (math.e ** (x) - math.e ** (-x)) / (math.e ** (x) + math.e ** (-x))  # tanh
y3 = np.where(x < 0, 0, x)  # relu

plt.xlim(-4, 4)
plt.ylim(-1, 1)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# Draw pic
plt.plot(x, y1, label='Sigmoid', linestyle="-", color="blue", linewidth=3)
plt.plot(x, y2, label='Tanh', linestyle="-", color="green", linewidth=3)
plt.plot(x, y3, label='ReLU', linestyle="-", color="red", linewidth=3)

# Title
plt.legend(['Sigmoid', 'Tanh', 'ReLU'], loc='best')

# save pic
plt.savefig('plot_test.png', dpi=100)

# show it!!
plt.show()
