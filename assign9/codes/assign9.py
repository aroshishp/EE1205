import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('assign9.dat')
s = data[:, 0]
G_s = data[:, 1]

plt.plot(s, G_s)
plt.xlabel('s')
plt.ylabel('G(s)')
plt.grid(True)
plt.savefig('assign9.png')
plt.show()