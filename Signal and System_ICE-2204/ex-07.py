import numpy as np
import matplotlib.pyplot as plt

# Input sequence
x = np.array([1, 2, 3, 4])

# Number of samples
N = len(x)


# ---------------- DFT ----------------

X = np.zeros(N, complex)

for k in range(N):
    for n in range(N):
        X[k] += x[n] * np.exp(-1j * 2 * np.pi * k * n / N)


# ---------------- IDFT ----------------

x2 = np.zeros(N, complex)

for n in range(N):
    for k in range(N):
        x2[n] += X[k] * np.exp(1j * 2 * np.pi * k * n / N)

x2 = x2 / N


# ---------------- Graphs ----------------

# Original signal
plt.subplot(3, 1, 1)
plt.stem(x)
plt.title("Original Sequence")
plt.grid()


# DFT magnitude
plt.subplot(3, 1, 2)
plt.stem(np.abs(X))
plt.title("DFT Magnitude")
plt.grid()


# IDFT signal
plt.subplot(3, 1, 3)
plt.stem(np.real(x2))
plt.title("Reconstructed Sequence")
plt.grid()

plt.tight_layout()
plt.show()


# Results
print("DFT =", X)
print("IDFT =", np.round(x2.real, 4))





# ## Experiment: Discrete Fourier Transform (DFT) and Inverse Discrete Fourier Transform (IDFT) Using MATLAB/Python

# ### Theory

# The **Discrete Fourier Transform (DFT)** is a mathematical technique used to convert a discrete-time signal from the **time domain to the frequency domain**. It helps to identify the frequency components present in a signal.

# For a sequence \(x[n]\) of length \(N\), DFT is defined as:

# $$
# X[k]=\sum_{n=0}^{N-1}x[n]e^{-j2\pi kn/N}
# $$

# where \(N\) is the number of samples, \(n\) is the time-domain index, and \(k\) is the frequency-domain index.

# The **Inverse Discrete Fourier Transform (IDFT)** converts the frequency-domain signal back into the original time-domain signal:

# $$
# x[n]=\frac{1}{N}\sum_{k=0}^{N-1}X[k]e^{j2\pi kn/N}
# $$

# In this experiment, DFT is used to transform a discrete signal into its frequency components, and IDFT is then used to reconstruct the original signal. MATLAB/Python can be used to implement and visualize both transformations.

# ### Objectives

# * To understand the concept of DFT and IDFT.
# * To implement DFT using MATLAB/Python.
# * To implement IDFT and reconstruct the original signal.
# * To observe the frequency components of a discrete signal.
# * To verify that IDFT of the DFT gives back the original signal.
