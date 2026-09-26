# Extract relevant features such as systolic peaks, diastolic points, and heart rate from 
# PPG signal.


import numpy as np
import matplotlib.pyplot as plt

# Basic settings
Fs = 100
duration = 6
t = np.linspace(0, duration, Fs * duration)

# Heart rate
heart_rate = 72
beat_time = 60 / heart_rate

# Create PPG signal
ppg = np.zeros_like(t)

for beat in np.arange(0, duration, beat_time):

    # Systolic and diastolic positions
    s = beat + 0.12
    d = beat + 0.35

    # Systolic peak
    ppg += np.exp(-((t - s) ** 2) / (2 * 0.02 ** 2))

    # Diastolic peak
    ppg += 0.4 * np.exp(-((t - d) ** 2) / (2 * 0.03 ** 2))


# Find systolic peaks
systolic = []

for i in range(1, len(ppg) - 1):
    if ppg[i] > ppg[i-1] and ppg[i] > ppg[i+1] and ppg[i] > 0.7:
        systolic.append(i)


# Find diastolic points
diastolic = []

for i in range(1, len(ppg) - 1):
    if ppg[i] > ppg[i-1] and ppg[i] > ppg[i+1] and 0.2 < ppg[i] < 0.6:
        diastolic.append(i)


# Calculate heart rate
peak_time = t[systolic]

if len(peak_time) > 1:
    avg_time = np.mean(np.diff(peak_time))
    hr = 60 / avg_time
else:
    hr = 0


# Plot
plt.plot(t, ppg, label="PPG Signal")
plt.plot(t[systolic], ppg[systolic], "ro", label="Systolic Peaks")
plt.plot(t[diastolic], ppg[diastolic], "go", label="Diastolic Points")

plt.title("PPG Signal Feature Extraction")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()

print("Estimated Heart Rate:", round(hr, 1), "bpm")




# 10. Feature Extraction from PPG Signal
# Theory

# Photoplethysmography (PPG) is a non-invasive technique used to measure changes in blood volume in tissue. A PPG waveform contains important information about the cardiac cycle. The major features of the waveform include the systolic peak, diastolic point, and the time interval between consecutive heartbeats.

# The systolic peak generally represents the maximum blood-volume change during a cardiac cycle, while the diastolic point occurs during the relaxation phase. By detecting consecutive systolic peaks, the time interval between heartbeats can be calculated and used to estimate the heart rate.

# The heart rate can be calculated as:

# $$ HR=\frac{60}{T} $$

# where \(T\) is the time interval between two consecutive beats in seconds.

# Objective
# To analyze a PPG signal.
# To detect systolic peaks and diastolic points.
# To calculate heart rate from the PPG signal.
# To visualize the important features of the PPG waveform.