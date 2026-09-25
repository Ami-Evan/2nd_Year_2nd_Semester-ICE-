import numpy as np                  # NumPy library
import matplotlib.pyplot as plt     # Graph আঁকার জন্য

# Time from 0 to 1 second
t = np.linspace(0, 1, 1000)

# Create three sine waves
y1 = np.sin(2 * np.pi * 2 * t)      # 2 Hz sine wave
y2 = np.sin(2 * np.pi * 5 * t)      # 5 Hz sine wave
y3 = np.sin(2 * np.pi * 10 * t)     # 10 Hz sine wave


# Plot 2 Hz sine wave
plt.subplot(3, 1, 1)
plt.plot(t, y1)
plt.title("Sine Wave - 2 Hz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()


# Plot 5 Hz sine wave
plt.subplot(3, 1, 2)
plt.plot(t, y2)
plt.title("Sine Wave - 5 Hz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()


# Plot 10 Hz sine wave
plt.subplot(3, 1, 3)
plt.plot(t, y3)
plt.title("Sine Wave - 10 Hz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()


# Adjust the graphs
plt.tight_layout()

# Show all graphs
plt.show()



# ## Theory

# A sinusoidal wave is a periodic signal commonly used in signal processing and communication systems. It can be represented as:

# $$
# x(t)=A\sin(2\pi ft+\phi)
# $$

# where \(A\) is the amplitude, \(f\) is the frequency, \(t\) is time, and \(\phi\) is the phase. Frequency determines the number of cycles completed per second. Higher frequency produces more cycles in the same time interval, while lower frequency produces fewer cycles. The time period is related to frequency by:

# $$
# T=\frac{1}{f}
# $$

# In this experiment, sinusoidal waves with different frequencies are generated and plotted using MATLAB/Python.

# ### Objectives

# * To generate sinusoidal waves with different frequencies.
# * To plot the generated signals using MATLAB/Python.
# * To observe the effect of frequency on the waveform.
# * To understand the relationship between frequency and time period.
