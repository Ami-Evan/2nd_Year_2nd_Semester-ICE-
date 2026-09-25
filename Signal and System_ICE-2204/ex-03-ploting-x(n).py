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




