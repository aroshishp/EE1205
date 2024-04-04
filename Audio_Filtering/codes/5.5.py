import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('5.5.dat')
n = data[:, 0]
y = data[:, 1]

plt.stem(n, y)
# plt.title('Filter Output using Convolution')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()
plt.savefig('figs/5.5.png')
plt.show()
