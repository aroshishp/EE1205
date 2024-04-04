import soundfile as sf
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np

#read .wav file 
input_signal, fs = sf.read('2.wav') 

#sampling frequency of Input signal
sampl_freq = fs
print(sampl_freq)

#order of the filter
order = 4

#cutoff frquency 
cutoff_freq = 6000.0  

#digital frequency
Wn = 2 * cutoff_freq / sampl_freq  

# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order, Wn, 'low') 

# get partial fraction expansion
r, p, k = signal.residuez(b, a)
print(r)
print(p)
print(k)


#number of terms of the impulse response
size = 40
sizelist = np.arange(size)

# using the general formula for h(n) (only r(i) and p(i) term)
def rp_vec(x):
    return np.sum(r * p**x)

# Apply the vectorized function to compute h(n)
h1 = np.vectorize(rp_vec)(sizelist)
#Pad the k(i) array with zeros to make same size as h1
k_add = np.pad(k, (0, size - len(k)), 'constant', constant_values=(0, 0))
#Net impulse response
h = h1 + k_add

# Plotting
plt.stem(sizelist, h)
plt.xlabel('n')
plt.ylabel('h(n)')
plt.grid()
plt.savefig("figs/7.2hn.png")
plt.show()
