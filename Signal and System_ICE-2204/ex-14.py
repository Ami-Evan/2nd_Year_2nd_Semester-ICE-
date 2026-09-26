# Determine the discrete-time Fourier transform and show magnitude, angle, real and 
# imaginary part of the following finite-duration sequence:                  at 501 
# equispaced frequency between       .

import numpy as np
import matplotlib.pyplot as plt

# Signal
x = [1, 2, 3, 4, 5]
n = [-1, 0, 1, 2, 3]

# Frequency
w = np.linspace(0, np.pi, 501)

# DTFT
X = []

for wi in w:
    X.append(sum(x[i] * np.exp(-1j * wi * n[i]) for i in range(5)))

X = np.array(X)

# 4 parts of DTFT
magnitude = abs(X)
phase = np.angle(X)
real = X.real
imag = X.imag


# Graphs
plt.subplot(4, 1, 1)
plt.plot(w, magnitude)
plt.title("Magnitude of DTFT")
plt.grid()

plt.subplot(4, 1, 2)
plt.plot(w, phase)
plt.title("Phase of DTFT")
plt.grid()

plt.subplot(4, 1, 3)
plt.plot(w, real)
plt.title("Real Part of DTFT")
plt.grid()

plt.subplot(4, 1, 4)
plt.plot(w, imag)
plt.title("Imaginary Part of DTFT")
plt.grid()

plt.tight_layout()
plt.show()



# ### Theory

# The **Discrete-Time Fourier Transform (DTFT)** is a mathematical tool used to represent a discrete-time signal in the frequency domain. It helps us understand how different frequency components are present in a discrete-time sequence.

# For a discrete sequence \(x(n)\), the DTFT is defined as:

# $$
# X(e^{j\omega})=\sum_{n=-\infty}^{\infty}x(n)e^{-j\omega n}
# $$

# For the given finite-duration sequence,

# $$
# x(n)=\{1,2,3,4,5\}
# $$

# the DTFT can be written as:

# $$
# X(e^{j\omega})
# =1+2e^{-j\omega}+3e^{-j2\omega}
# +4e^{-j3\omega}+5e^{-j4\omega}
# $$

# The DTFT is a complex-valued function and can be analyzed through its **magnitude, phase, real part, and imaginary part**. The magnitude spectrum shows the strength of the frequency components, while the phase spectrum represents their phase information.

# In this experiment, the frequency range \(0\leq\omega\leq\pi\) is divided into **501 equally spaced points**. These points are used to calculate and plot the magnitude, phase, real, and imaginary parts of the DTFT.


# Objective
# To determine the discrete-time Fourier transform of a finite-duration sequence.
# To plot the magnitude and phase spectrum of the sequence.
# To observe the real and imaginary parts of the DTFT.
# To analyze the frequency characteristics of the given sequence.