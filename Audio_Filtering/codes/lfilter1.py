import numpy as np

def custom_lfilter(b, a, x):
    """
    Custom implementation of the lfilter function.

    Parameters:
        b (array_like): Numerator coefficients of the filter.
        a (array_like): Denominator coefficients of the filter.
        x (array_like): Input data.

    Returns:
        array_like: Output of the filter.
    """
    # Initialize output array
    y = np.zeros_like(x)
    
    # Apply the filter
    for n in range(len(x)):
        y[n] = np.dot(b, x[max(0, n - len(b) + 1):n + 1])
        if len(a) > 1:
            y[n] -= np.dot(a[1:], y[max(0, n - len(a) + 1):n][::-1])

    return y

# Now, let's use both lfilter and custom_lfilter and plot the results

import soundfile as sf
import matplotlib.pyplot as plt
from scipy import signal

# Read the audio file
input_signal, fs = sf.read('2.wav')

# Order of the filter
order = 4

# Cutoff frequency 6kHz
cutoff_freq = 6000.0

# Digital frequency
Wn = 2 * cutoff_freq / fs

# b and a are numerator and denominator polynomials, respectively
b, a = signal.butter(order, Wn, 'low')

# Filter the audio using signal.lfilter
output_signal_lfilter = signal.lfilter(b, a, input_signal)

# Filter the audio using custom function
output_signal_custom = custom_lfilter(b, a, input_signal)

# Plot the original and filtered signals
plt.figure(figsize=(12, 6))
plt.plot(input_signal, label='Original Audio')
plt.plot(output_signal_lfilter, label='Filtered Audio (lfilter)')
plt.plot(output_signal_custom, label='Filtered Audio (Custom)')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.title('Comparison of Filtered Audio')
plt.legend()
plt.show()
