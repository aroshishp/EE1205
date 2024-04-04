import numpy as np
from numpy.fft import fft, ifft
import matplotlib.pyplot as plt


N = 14
n = np.arange(N)
fn = (-1/2)**n
hn1 = np.pad(fn, (0,2), 'constant', constant_values=(0,0))
hn2 = np.pad(fn, (2,0), 'constant', constant_values=(0,0))
h = hn1 + hn2
xtemp = np.array([1.0,2.0,3.0,4.0,2.0,1.0])
x = np.pad(xtemp, (0,10), 'constant', constant_values=(0))

#define the DFT matrix
W = fft(np.eye(len(x)))

#Calculate X and H using matrix method
X = x @ W
H = h @ W

Y = H * X

#Inverse of DFT matrix
Winv= np.linalg.inv(W)

#IDFT from matrix method
y = (Y @ Winv).real

plt.stem(range(0,16),y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()
plt.savefig('figs/6.5.png')
plt.show()
# plt.savefig('yn_DFT_matrix.png')