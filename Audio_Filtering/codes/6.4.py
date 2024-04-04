import numpy as np
import matplotlib.pyplot as plt

N = 18
n = np.arange(N)
fn = (-1 / 2)**n
hn1 = np.pad(fn, (0, 2), 'constant', constant_values=(0))
hn2 = np.pad(fn, (2, 0), 'constant', constant_values=(0))
h = hn1 + hn2
 
xtemp = np.array([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
x = np.pad(xtemp, (0, 12), 'constant', constant_values=(0))

X = np.zeros(N) + 1j * np.zeros(N)
for k in range(0, N):
	for n in range(0, N):
		X[k] += x[n] * np.exp(-1j * 2 * np.pi * n * k / N)
		
H = np.zeros(N) + 1j * np.zeros(N)
for k in range(0, N):
	for n in range(0, N):
		H[k] += h[n] * np.exp(-1j * 2 * np.pi * n * k / N)
 
Y = np.zeros(N) + 1j * np.zeros(N)
for k in range(0, N):
	Y[k] = X[k] * H[k]

y = np.zeros(N) + 1j * np.zeros(N)
for k in range(0, N):
	for n in range(0, N):
		y[k] += Y[n] * np.exp(1j * 2 * np.pi * n * k / N)

y = np.real(y)/N

#pad x to ensure same size
x_padded = np.pad(x, (0, len(h) - len(x)))

# Perform FFT
X_fft = np.fft.fft(x_padded)
X_np = np.fft.fft(x)
H_fft = np.fft.fft(h)

Y_fft = H_fft * X_fft

y_ifft = np.fft.ifft(Y_fft).real
#plots
plt.stem(range(0, N), y, linefmt='b-', markerfmt='bo')
plt.plot(range(0, N), y_ifft[:N], 'mo', marker='o')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid(True)
plt.legend(['From IFFT', 'From IDFT'])
plt.savefig('figs/6.4.png')
plt.show()
plt.clf()
