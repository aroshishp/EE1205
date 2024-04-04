import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('5.2.dat')
n = data[:, 0]
h = data[:, 1]

plt.stem(n, h)
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.grid()
plt.savefig('figs/5.2.png')
plt.show()
