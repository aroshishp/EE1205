# import numpy as np
# import matplotlib.pyplot as plt

# n = np.arange(10)
# fn=(-1/2)**n

# #(-1/2)^n u(n), add two zeros at end
# hn1=np.pad(fn, (0,2), 'constant', constant_values=(0))

# #(-1/2)^(n-2)u(n-2), add two zeros at beginning of array, which symbolizes
# #introducing a delay/forward shift of 2
# hn2=np.pad(fn, (2,0), 'constant', constant_values=(0))

# #Plot the impulse response
# plt.stem(np.arange(12), hn1+hn2)
# # plt.title('Filter Impulse Response')
# plt.xlabel('$n$')
# plt.ylabel('$h(n)$')
# plt.grid()
# plt.savefig('figs/5.2.png')
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Load data from the .dat file
data = np.loadtxt('5.2.dat')
n = data[:, 0]
h = data[:, 1]

# Plotting
plt.stem(n, h)
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.grid()
plt.savefig('figs/5.2.png')
plt.show()