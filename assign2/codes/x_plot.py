import matplotlib.pyplot as plt
import numpy as np

def x(n, q):
    return 2 * q * n * (n >= 0)

q = 0.5

n_values = np.arange(-6, 7, 1)
x_values = x(n_values, q)

plt.stem(n_values, x_values, linefmt='b-', markerfmt='bo', basefmt='r')
plt.title('Plot of x(n) vs n')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.savefig('x_plot.png')
#plt.show()
