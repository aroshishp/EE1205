# import matplotlib.pyplot as plt
# import numpy as np

# def Z(R1, R2, L1, C1, w):
#     return R2 + 1j*w*L1 + (R1)/(1+1j*w*R1*C1)

# w = np.linspace(0, 4000, 10000)
# R1 = 20
# R2 = 4
# C1 = 0.001/np.pi
# L1 = 0.02/np.pi

# Z_out = Z(R1, R2, L1, C1, w)

# plt.plot(w, np.abs(Z_out))
# plt.xlabel('$\omega$')
# plt.ylabel('Magnitude of $z_{eff}$')
# plt.grid(True)
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Load data from the file
data = np.loadtxt('assign6.dat')
Z_real = data[:, 0]
Z_imag = data[:, 1]

# Calculate magnitude of impedance
Z_mag = np.abs(Z_real + 1j * Z_imag)

# Generate frequencies
w = np.linspace(0, 4000, len(Z_mag))

# Plot
plt.plot(w, Z_mag)
plt.xlabel('$\omega$')
plt.ylabel('Magnitude of $z_{eff}$')
plt.grid(True)
plt.savefig('Zplot.png')
plt.show()
