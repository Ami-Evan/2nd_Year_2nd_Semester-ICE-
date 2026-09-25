import numpy as np
import matplotlib.pyplot as plt

# Input
x = np.array([1, 2, 3, 4])

# Impulse response
h = np.array([1, 1, 1])

# Convolution
y = np.convolve(x, h)

plt.figure(figsize=(8, 6))

# 1. Input sequence
plt.subplot(3, 1, 1)
plt.stem(range(len(x)), x)
plt.title("Input Sequence x(n)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()

# 2. Impulse response
plt.subplot(3, 1, 2)
plt.stem(range(len(h)), h)
plt.title("Impulse Response h(n)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()

# 3. Convolution result
plt.subplot(3, 1, 3)
plt.stem(range(len(y)), y)
plt.title("Convolution Result y(n)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()

print("y =", y)





# Theory
# Convolution is a fundamental mathematical operation in signal processing and
# system analysis. It describes how an input signal interacts with a system's impulse
# response to produce an output signal. In simple terms, convolution helps determine
# the response of a system when an input is applied.
# Mathematical Definition of Convolution
# For continuous-time signals, convolution is defined as:
# y(t)= (x∗ h) (t)= ∫ x(τ)h(t − τ)dτ ∞

# −∞

# where:
# • x(t)is the input signal,
# • h(t) is the impulse response of the system,
# • y(t) is the output signal,
# • τ is a dummy variable for integration,
# • (x ∗ h) (t)denotes the convolution operation.
# For discrete-time signals (used in digital signal processing), convolution
# is represented as:
# y[n] = (x ∗h) [n]=∑∞

# −∞ x[k]h[n − k]

# where:
# • x[n] is the discrete input signal,
# • h[n] is the discrete impulse response,
# • y[n] is the discrete output signal,
# • The summation runs over all integer values of k.

# Objective
# To perform discrete-time convolution using Python.