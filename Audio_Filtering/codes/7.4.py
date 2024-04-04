import numpy as np
import matplotlib.pyplot as plt

# Read data from fft.txt
conv_times = np.loadtxt('conv.txt')

# Read data from conv.txt
fft_times = np.loadtxt('fft.txt')


sizes = np.array([2**i for i in range(16)])

# Plotting
plt.stem(sizes, fft_times, markerfmt='bo', linefmt = 'b-', label='FFT + IFFT Time')
plt.stem(sizes, conv_times,markerfmt='ro', linefmt = 'r-',label='Convolution Time')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.xscale('log', base=2)
plt.yscale('log')
plt.legend()
plt.grid(True)
plt.savefig("figs/7.4.png")
plt.show()