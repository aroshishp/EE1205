import matplotlib.pyplot as plt
import numpy as np

# Impedance Function |H(jω)|
def magnitude_H(omega, R, L, C):
    return np.sqrt(R**2 + (omega * L - 1/(omega * C))**2)

R_value = 7.4
L_value = 3
C_value = 0.000027

omega_values = np.logspace(0, 3, 10000)

magnitude_values = magnitude_H(omega_values, R_value, L_value, C_value)

plt.plot(np.log10(omega_values), magnitude_values, label='|H(jω)|')
plt.xlabel('log($\omega$)')
plt.ylabel('|H(j$\omega$)|')
plt.title('Magnitude Plot of H(j$\omega$)')

plt.ylim(0, 30)
plt.xlim(2, 2.1)

plt.legend()

plt.grid(True)
plt.savefig('h_plot.png', dpi = 300, bbox_inches = 'tight')
