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