# Show Fourier series approximation of square wave: 
      
#   [          
            
            
#             ] 

import numpy as np
import matplotlib.pyplot as plt

# Time
t = np.linspace(0, 2 * np.pi, 1000)

# Fourier Series
def square_wave(t, n):
    x = 0

    for k in range(1, 2 * n, 2):
        x = x + np.sin(k * t) / k

    return (4 / np.pi) * x


# 1, 2 and 4 terms
y1 = square_wave(t, 1)
y2 = square_wave(t, 2)
y4 = square_wave(t, 4)


# 1 term
plt.subplot(3, 1, 1)
plt.plot(t, y1)
plt.title("1 Term")
plt.grid()

# 2 terms
plt.subplot(3, 1, 2)
plt.plot(t, y2)
plt.title("2 Terms")
plt.grid()

# 4 terms
plt.subplot(3, 1, 3)
plt.plot(t, y4)
plt.title("4 Terms")
plt.grid()

plt.tight_layout()
plt.show()




# Objective
# To generate a square wave using Fourier series.
# To study the approximation of a square wave using odd harmonics.
# To observe how increasing the number of harmonics improves the square wave approximation.

# ### Theory

# A square wave is a periodic signal that can be represented as a combination of sinusoidal waves using **Fourier series**. For a symmetrical square wave, only the **odd harmonics** are present.

# $$
# x(t)=\frac{4}{\pi}\left[
# \sin(\omega_0t)
# +\frac{1}{3}\sin(3\omega_0t)
# +\frac{1}{5}\sin(5\omega_0t)+\cdots
# \right]
# $$

# where,

# $$
# \omega_0=2\pi f_0
# $$

# Here, \(f_0\) is the fundamental frequency. As more odd harmonics are added, the generated waveform becomes closer to the
# original square wave. Thus, Fourier series helps us understand how a complex square wave can be constructed from simple 
# sinusoidal components.
