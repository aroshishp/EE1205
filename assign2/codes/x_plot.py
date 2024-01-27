import numpy as np
import matplotlib.pyplot as plt

# Function to calculate x(n)
def x_n(n, q):
    u_n = 1 if n >= 0 else 0
    delta_n = 1 if n == 0 else 0
    return 2 * q * ((n - 1) * u_n + delta_n)

# Value for q
q_value = 0.5

# Range of n from -6 to 6
n_values = np.arange(-6, 7, 1)

# Calculate x(n) for each value of n
x_values = [x_n(n, q_value) for n in n_values]

# Plotting
plt.stem(n_values, x_values, linefmt='b-', markerfmt='bo', basefmt='r')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid(True)
plt.savefig('x_plot.png')
plt.show()
