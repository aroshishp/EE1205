import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy import signal
from scipy.fft import fft, ifft

x, fs = sf.read('2.wav')

#order
order = 4

# Cutoff frequency 4kHz
cutoff_freq = 6000.0

# Digital frequency
Wn = 2 * cutoff_freq / fs
b, a = signal.butter(order, Wn, 'low')

N = 30
impulse = np.zeros(N)
impulse[0] = 1
h = signal.lfilter(b, a, impulse)
print(len(h))

input_signal = [subplot[0] for subplot in x]

xtemp = input_signal[585:615]

#convolution
y_convolve = np.convolve(xtemp, h)

# Perform signal filtering using scipy.signal.lfilter
y_scipy = signal.lfilter(b , a , xtemp)

plt.stem(xtemp)
plt.xlabel('$n$')
plt.ylabel('$x(n)$')
plt.legend()
plt.grid()
plt.savefig('figs/input.png')
plt.show()

plt.stem(range(0,N),y_scipy,markerfmt='bo',basefmt = 'k',linefmt = 'ro-',label ='sciPY')
plt.stem(range(0, N), y_convolve[:N], markerfmt='ro',basefmt = 'k',linefmt = 'co-', label='Convolution')

plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.legend()
plt.grid()
plt.savefig('figs/output.png')
plt.show()