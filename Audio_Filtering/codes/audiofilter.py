import soundfile as sf
from scipy import signal

# Read .wav file
input_signal, fs = sf.read('2.wav')

# Order of the filter
order = 4

# Cutoff frequency 6kHz
cutoff_freq = 6000.0

# Digital frequency
Wn = 2 * cutoff_freq / fs

# b and a are numerator and denominator polynomials, respectively
b, a = signal.butter(order, Wn, 'low')

print(a)
print(b)

output_signal = signal.lfilter(b,a, input_signal)
# Write the output signal into a .wav file
sf.write('2_fil.wav', output_signal, fs)