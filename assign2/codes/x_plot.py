import matplotlib.pyplot as plt
import numpy as np

q = 0.5

n_values = np.arange(-6, 7, 1)
x_values = 2 * q * n_values * (n_values >= 0)

plt.stem(n_values, x_values, linefmt='b-', markerfmt='bo', basefmt='r')
plt.title('Plot of x(n) vs n')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.savefig('x_plot.png')
#plt.show()
