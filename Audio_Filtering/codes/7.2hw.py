import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import soundfile as sf

#sampling frequency obtained from the audio file
input_signal, fs = sf.read('2.wav')

#order of the filter
order=4

#cutoff frquency 4kHz
cutoff_freq=6000.0 

#digital frequency
Wn=2*cutoff_freq/fs 


# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order, Wn, 'low') 

#DTFT
def H(z):
	num = np.polyval(b,z**(-1))
	den = np.polyval(a,z**(-1))
	H = num/den
	return H
		
omega = np.linspace(0,np.pi,100)

plt.plot(omega, abs(H(np.exp(1j*omega))))
plt.xlabel('$\omega$')
plt.ylabel('$|H(e^{\jmath\omega})| $')
plt.grid()
plt.savefig("figs/7.2hw.png")
plt.show()