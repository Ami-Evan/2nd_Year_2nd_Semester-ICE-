# Show Power Density Spectrum of a Square Wave. 

import numpy as np
import matplotlib.pyplot as plt

# Time
Fs = 1000
t = np.linspace(0, 1, Fs, endpoint=False)

# 5 Hz square wave
square = np.sign(np.sin(2 * np.pi * 5 * t))

# FFT
X = np.fft.fft(square)

# Frequency
freq = np.fft.fftfreq(len(t), 1 / Fs)

# Power
power = abs(X) ** 2 / len(t)

# First half
n = len(t) // 2

# Square wave
plt.subplot(2, 1, 1)
plt.plot(t, square)
plt.title("Square Wave (5 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

# Power spectrum
plt.subplot(2, 1, 2)
plt.stem(freq[:n], power[:n])
plt.title("Power Density Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power")
plt.xlim(0, 100)
plt.grid()

plt.tight_layout()
plt.show()




# 11. Power Density Spectrum of a Square Wave
# Theory

# The Power Density Spectrum (PDS) describes how the power of a signal is distributed among different frequency components. A square wave is a periodic signal that contains a fundamental frequency along with several harmonic frequencies.

# The frequency components of a square wave mainly consist of the odd harmonics of its fundamental frequency,
# such as the 1st, 3rd, 5th, 7th harmonics, and so on. The power of these harmonic components decreases as the harmonic 
# frequency increases. By plotting the Power Density Spectrum, the distribution of power at different frequencies can be 
# observed clearly.
# This experiment helps to understand the frequency-domain characteristics of a square wave.


# Objective
# To generate a square wave signal.
# To calculate its frequency spectrum.
# To determine and plot the Power Density Spectrum.
# To observe the fundamental frequency and harmonic components of the square wave