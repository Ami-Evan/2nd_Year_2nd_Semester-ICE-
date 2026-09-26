# To find the amplitude spectrum of the multi frequency signal:  
                                                                              
# And also show approximate the Fourier transform integral for 0 ≤ f ≤ 900 Hz. 

import numpy as np
import matplotlib.pyplot as plt

Fs = 2000
t = np.arange(0, 1, 1 / Fs)

# Signal
x = np.cos(2*np.pi*100*t) + np.cos(2*np.pi*500*t) + np.cos(2*np.pi*700*t)

# FFT
X = np.fft.fft(x)
freq = np.fft.fftfreq(len(x), 1/Fs)

# Manual Fourier Transform
f = np.linspace(0, 900, 900)
X2 = []

for i in f:
    y = np.sum(x * np.exp(-1j * 2*np.pi*i*t))
    X2.append(abs(y) / Fs)


# Original signal
plt.subplot(3, 1, 1)
plt.plot(t[:200], x[:200])
plt.title("Original Signal")
plt.grid()

# FFT
plt.subplot(3, 1, 2)
n = len(x) // 2
plt.stem(freq[:n], abs(X[:n]) * 2 / len(x))
plt.title("FFT Spectrum")
plt.xlim(0, 900)
plt.grid()

# Fourier Transform
plt.subplot(3, 1, 3)
plt.plot(f, X2)
plt.title("Fourier Transform")
plt.grid()

plt.tight_layout()
plt.show()





# ### Theory

# A multi-frequency signal is a signal that contains two or more sinusoidal components with different frequencies. Such signals are commonly used in signal processing to study the frequency characteristics of a combined signal.

# The given multi-frequency signal is:

# $$
# x(t)=\cos(2\pi100t)+\cos(2\pi500t)+\cos(2\pi700t)
# $$

# This signal consists of three sinusoidal components with frequencies **100 Hz, 500 Hz, and 700 Hz**. Each component contributes to the overall signal in the time domain.

# The **Fourier Transform (FT)** converts a time-domain signal into its corresponding frequency-domain representation. The **amplitude spectrum** shows the magnitude of different frequency components present in the signal. Therefore, peaks are expected at **100 Hz, 500 Hz, and 700 Hz** in the amplitude spectrum.

# In this experiment, the Fourier transform is approximately observed over the frequency range:

# $$
# 0\leq f\leq900\text{ Hz}
# $$

# Thus, the amplitude spectrum helps to identify and analyze the individual frequency components of the multi-frequency signal.



# Objective
# To generate a multi-frequency signal containing different sinusoidal components.
# To determine the amplitude spectrum of the signal.
# To identify the frequency components present in the signal.
# To observe the approximate Fourier transform for \(0\leq f\leq900\) Hz.
