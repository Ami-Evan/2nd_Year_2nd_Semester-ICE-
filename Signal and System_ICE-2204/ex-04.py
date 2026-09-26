# Plot following signal operations using user defined function  - i) Addition ii) Folding 
#                 iii) Signal shifting 

import numpy as np
import matplotlib.pyplot as plt


# User Defined Function for Addition
def addition(x1, x2):
    return x1 + x2


# User Defined Function for Folding
def folding(x):
    return x[::-1]


# User Defined Function for Shifting
def shifting(x, k):
    return np.roll(x, k)


# Original Signals(sample index)
n = np.arange(5)

x1 = np.array([1, 2, 3, 2, 1])
x2 = np.array([1, 1, 2, 1, 1])


# Addition
y_add = addition(x1, x2)


# Folding
x = np.array([1, 2, 3, 4, 5])
y_fold = folding(x)


# Shifting
k = int(input("Enter shifting value: "))
y_shift = shifting(x, k)


# -------- All Graphs in One Window --------

plt.figure(figsize=(10, 8))


# 1. Original Signal
plt.subplot(2, 2, 1)
plt.stem(n, x1)
plt.xlabel("n")
plt.ylabel("x(n)")
plt.title("Original Signal")
plt.grid(True)


# 2. Addition
plt.subplot(2, 2, 2)
plt.stem(n, y_add)
plt.xlabel("n")
plt.ylabel("y(n)")
plt.title("Addition of Two Signals")
plt.grid(True)


# 3. Folding
plt.subplot(2, 2, 3)
plt.stem(n, y_fold)
plt.xlabel("n")
plt.ylabel("x(-n)")
plt.title("Folding of Signal")
plt.grid(True)


# 4. Shifting
plt.subplot(2, 2, 4)
plt.stem(n, y_shift)
plt.xlabel("n")
plt.ylabel("x(n-2)")
plt.title("Shifting of Signal")
plt.grid(True)


plt.tight_layout()
plt.show()




# Theory
# Signal operations include basic transformations such as addition, shifting (time delay
# or advance), and folding (time reversal). These operations are fundamental in signal
# processing.
# 1. Signal Addition
# Signal addition is a basic arithmetic operation where two signals are added point-by-point.
# Mathematically, if we have two discrete-time signals x1(n) and x2(n) their sum is given by:
# y(n)=x1(n)+x2(n)
# 2. Shifting (Time Shifting)
# Time shifting modifies a signal by shifting it forward (delay) or backward (advance) along the
# time axis.
# • Right Shift (Delay): y(n)=x(n−k), where k>0
# • Left Shift (Advance): y(n) = x(n+k), where k>0

# 3. Folding (Time Reversal)
# Folding, also known as time reversal, reflects a signal about n=0 Mathematically:
# y(n)=x(−n)

# Objective
# To perform addition, shifting, and folding of discrete-time signals in Python.