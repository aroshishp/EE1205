import numpy as np
import matplotlib.pyplot as plt

# Load data from .dat file
data = np.loadtxt('assign9.dat')
Gjw = data[:,0] + 1j * data[:,1]

# Frequency range
w = np.linspace(-2, 2, len(data))

# Plot
plt.plot(w, np.abs(Gjw))
plt.xlabel('$\omega$')
plt.ylabel('|G(jw)|')
plt.grid(True)
plt.show()
