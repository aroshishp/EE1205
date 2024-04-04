import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('3.2.dat')
n = data[:, 0]
y = data[:, 1]

plt.stem(n, y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()
plt.savefig('figs/3.2.png')
plt.show()