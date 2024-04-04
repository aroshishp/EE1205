import numpy as np
import matplotlib.pyplot as plt

# Load data from the .dat file
data = np.loadtxt('5.4.dat')
n = data[:, 0]
h = data[:, 1]

# Plotting
plt.stem(n, h)
# plt.title('Impulse Response Definition')
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.grid()
plt.savefig('figs/5.4.png')
plt.show()
