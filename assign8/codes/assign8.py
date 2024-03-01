import matplotlib.pyplot as plt
import numpy as np

# Read data from the .dat file
data = np.loadtxt('assign8.dat')
n_values = data[:, 0]
x = data[:, 1]
y = data[:, 2]

# Plot x_n
plt.stem(n_values, x, linefmt='b-', basefmt='r-', markerfmt='bo')
plt.xlim(-5, 10)
plt.grid(True)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.savefig('x_plt.png')
plt.show()

# Plot y_n
plt.stem(n_values, y, linefmt='b-', basefmt='r-', markerfmt='bo')
plt.xlim(-5, 6)
plt.ylim(0, 1.75)
plt.grid(True)
plt.xlabel('n')
plt.ylabel('y(n)')
plt.savefig('y_plt.png')
plt.show()