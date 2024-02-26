import numpy as np
import matplotlib.pyplot as plt

# Load data from the .dat file
data = np.loadtxt('assign5.dat')
omega = data[:, 0]
V_out_values = data[:, 1]

# Plot V_out vs. omega
plt.plot(omega, V_out_values, color='blue')
plt.xlabel('$\omega$')
plt.ylabel('$V_{out}(t)$')
plt.grid(True)
plt.savefig('V_out_plot.png')
plt.show()
