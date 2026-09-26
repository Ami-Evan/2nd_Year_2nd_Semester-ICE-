# Determine and plot the following sequences.                      ,    
#         .

import numpy as np
import matplotlib.pyplot as plt

# n values
n = np.arange(-7, 8)

# Unit impulse
delta1 = (n == -2)
delta2 = (n == 4)

# Sequence
x = 2 * delta1 - delta2

# Plot
plt.stem(n, x)

plt.xlabel("n")
plt.ylabel("X(n)")
plt.title("X(n) = 2δ(n+2) - δ(n-4)")

plt.grid(True)
plt.show()


# Experiment 3: Determine and Plot the Sequence
# Theory

# A discrete-time signal is represented as a sequence of values defined at discrete time instants. 
# The unit impulse or unit sample sequence, denoted by \(\delta(n)\), is one of the basic discrete-time signals.
#  It has a value of 1 at \(n=0\) and 0 at all other values of \(n\). By shifting the impulse, it can be placed at 
# different positions on the time axis. For example, \(\delta(n+2)\) represents an 
# impulse at \(n=-2\), while \(\delta(n-4)\) represents an impulse at \(n=4\).

# The given sequence is

# $$ x(n)=2\delta(n+2)-\delta(n-4),\qquad -7\leq n\leq7 $$

# Here, \(2\delta(n+2)\) produces an impulse with amplitude 2 at \(n=-2\), and \(-\delta(n-4)\) produces 
# an impulse with amplitude -1 at \(n=4\). All other values of the sequence are zero. By plotting this sequence,
#  the position, direction, and amplitude of the shifted impulses can be clearly observed.

# Objectives
# To understand the concept of the unit impulse sequence.
# To study the shifting and scaling properties of an impulse.
# To determine the values of the given discrete-time sequence.
# To plot the sequence for the specified range of \(n\).
# To observe the amplitude and location of the impulses.


