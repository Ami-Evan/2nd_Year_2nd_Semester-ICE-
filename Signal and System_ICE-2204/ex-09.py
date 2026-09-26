# Removing Noise from an Audio Signal 
#   Steps: 
# a.    Generate an audio signal (a pure sine wave of 440 Hz). 
# b. Add random noise. 
# c. Apply DFT to transform the signal to the frequency domain. 
# d. Remove noise by filtering high frequencies. 
# e. Apply Inverse DFT to get back the cleaned signal. 


import numpy as np
import matplotlib.pyplot as plt

# Sampling frequency
Fs = 5000

# Time
t = np.linspace(0, 0.02, int(0.02 * Fs), endpoint=False)

# 440 Hz clean signal
signal = np.sin(2 * np.pi * 440 * t)

# Add noise
np.random.seed(0)
noise = 0.5 * np.random.randn(len(t))
noisy = signal + noise

# FFT
X = np.fft.fft(noisy)

# Frequency
freq = np.fft.fftfreq(len(t), 1 / Fs)

# Remove frequencies above 600 Hz
X[np.abs(freq) > 600] = 0

# IDFT
cleaned = np.fft.ifft(X).real


# 1. Noisy signal
plt.subplot(3, 1, 1)
plt.plot(t, noisy)
plt.title("Noisy Audio Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()


# 2. Frequency spectrum
plt.subplot(3, 1, 2)
plt.plot(freq[:len(freq)//2], np.abs(np.fft.fft(noisy))[:len(freq)//2])
plt.title("Spectrum of Noisy Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid()


# 3. Cleaned signal
plt.subplot(3, 1, 3)
plt.plot(t, cleaned)
plt.title("Cleaned Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()

print("Done")




# 9. Removing Noise from an Audio Signal
# Theory

# An audio signal may contain unwanted components called noise, which can reduce the quality of the signal. In this experiment, a pure sinusoidal audio signal of 440 Hz is generated as the original signal. Random noise is then added to simulate a noisy audio signal.

# The noisy signal is transformed from the time domain to the frequency domain using the Discrete Fourier Transform (DFT). In the frequency domain, the signal and noise can be analyzed based on their frequency components. A suitable filter is then used to remove unwanted high-frequency components. Finally, the Inverse DFT (IDFT) is 
# applied to convert the filtered signal back to the time domain and obtain the cleaned audio signal.

# Objective
# To generate a 440 Hz audio signal.
# To add random noise to the signal.
# To apply DFT and observe the frequency components.
# To remove high-frequency noise using filtering.
# To reconstruct the cleaned signal using IDFT.