import matplotlib.pyplot as plt
import numpy as np

#set p = q = 0.5
q = 0.5

#create discrete values of n
n_values = np.arange(-6, 7, 1)
#create corresponding vlaues of x(n)
x_values = 2 * q * n_values * (n_values >= 0)

#create stem plot
plt.stem(n_values, x_values, linefmt='b-', markerfmt='bo', basefmt='r')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.savefig('x_plot.png')
plt.show()
