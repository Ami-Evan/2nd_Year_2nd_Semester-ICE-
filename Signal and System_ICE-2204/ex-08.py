# Find the spectrum of the following signal:  
#                                                                 .

import numpy as np
import matplotlib.pyplot as plt

# Sampling frequency
Fs = 100

# Time values
t = np.arange(0, 1, 1/Fs)

# Create the signal
x = 0.25 + 2*np.sin(2*np.pi*5*t) \
    + np.sin(2*np.pi*12.5*t) \
    + 1.5*np.sin(2*np.pi*20*t) \
    + 0.5*np.sin(2*np.pi*35*t)

# Number of samples
N = len(x)

# Calculate FFT
X = np.fft.fft(x)

# Frequency values
freq = np.fft.fftfreq(N, 1/Fs)

# Take positive half
half = N // 2


# -------- Original Signal --------

plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title("Signal x(t)")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()


# -------- Amplitude Spectrum --------

plt.subplot(2, 1, 2)
plt.stem(freq[:half], np.abs(X[:half]) * 2 / N)
plt.title("Amplitude Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.grid()


# Show graphs
plt.tight_layout()
plt.show()

print("Done")






# Experiment 8: Find the Spectrum of the Given Signal
# Theory

# The spectrum of a signal represents the different frequency components present in the signal and their corresponding magnitudes. A time-domain signal may contain several sinusoidal components of different frequencies and amplitudes. Fourier analysis is used to transform such a signal from the time domain into the frequency domain, where its individual frequency components can be easily identified.

# The given signal is

# $$ x(k)=0.25+2\sin(2\pi5k)+\sin(2\pi12.5k) +1.5\sin(2\pi20k)+0.5\sin(2\pi35k) $$

# The signal contains a DC component of 0.25 and several sinusoidal components with frequencies of 5 Hz, 12.5 Hz, 20 Hz, and 35 Hz. The amplitudes of these sinusoidal components are 2, 1, 1.5, and 0.5 respectively. Using Fourier Transform, the signal can be represented in the frequency domain. The magnitude spectrum shows peaks at the frequencies contained in the signal. Thus, spectrum analysis helps us identify the frequency content and relative strength of the components present in a composite signal.

# Objectives
# To understand the concept of frequency spectrum.
# To analyze a composite signal in the frequency domain.
# To identify the different frequency components present in the given signal.
# To calculate the Fourier Transform of the signal.
# To plot the magnitude spectrum and observe the frequency peaks.
# To understand the relationship between time-domain and frequency-domain representations.