import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('4.5.dat')
omega = data[:, 0]
H_abs = data[:, 1]

plt.plot(omega, H_abs)
plt.xlabel('$\omega$')
plt.ylabel('$|H(e^{j\omega})|$')
plt.grid()
w_ticks = [-3*np.pi, -2*np.pi, -np.pi, 0, np.pi, 2*np.pi, 3*np.pi]
w_labels = ['$-3\pi$', '$-2\pi$', '$-\pi$', '$0$', '$\pi$', '$2\pi$', '$3\pi$']
plt.xticks(w_ticks, w_labels)
plt.savefig('figs/4.5.png')
plt.show()