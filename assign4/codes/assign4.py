import numpy as np
import matplotlib.pyplot as plt

# Load data from .dat file
data = np.loadtxt('rc_data.dat')
t = data[:, 0]
V_out = data[:, 1]

# Plot
plt.plot(t, V_out)
plt.xlabel('Time (s)')
plt.ylabel('$V_{out}$')
plt.grid(True)
plt.savefig('assign4.png')
plt.show()

