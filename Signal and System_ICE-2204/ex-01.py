import numpy as np
import matplotlib.pyplot as plt

# n = -10 to 10
n = np.arange(-10, 11)

# Unit sample
sample = np.where(n == 0, 1, 0)

# Unit step
step = np.where(n >= 0, 1, 0)

# Unit ramp
ramp = np.where(n >= 0, n, 0)


# Unit sample graph
plt.subplot(3, 1, 1)
plt.stem(n, sample)
plt.title("Unit Sample Sequence")
plt.grid()

# Unit step graph
plt.subplot(3, 1, 2)
plt.stem(n, step)
plt.title("Unit Step Sequence")
plt.grid()

# Unit ramp graph
plt.subplot(3, 1, 3)
plt.stem(n, ramp)
plt.title("Unit Ramp Sequence")
plt.grid()

plt.tight_layout()
plt.show()


# ## Experiment: Elementary Discrete Signals

# ### Theory

# Elementary discrete-time signals are the basic signals used in **Digital Signal Processing (DSP)**. They are defined at discrete integer values of time \(n\). The three important elementary signals are the **unit sample sequence, unit step signal, and unit ramp signal**.

# **i) Unit Sample Sequence:**
# The unit sample sequence, denoted by \(\delta[n]\), has a value of 1 at \(n=0\) and 0 at all other values of \(n\).

# $$
# \delta[n]=
# \begin{cases}
# 1, & n=0\\
# 0, & n\neq0
# \end{cases}
# $$

# **ii) Unit Step Signal:**
# The unit step signal, denoted by \(u[n]\), has a value of 1 for \(n\geq0\) and 0 for \(n<0\).

# $$
# u[n]=
# \begin{cases}
# 1, & n\geq0\\
# 0, & n<0
# \end{cases}
# $$

# **iii) Unit Ramp Signal:**
# The unit ramp signal is denoted by \(r[n]\). Its value increases linearly with \(n\) for \(n\geq0\) and is 0 for negative values of \(n\).

# $$
# r[n]=
# \begin{cases}
# n, & n\geq0\\
# 0, & n<0
# \end{cases}
# $$

# These signals are fundamental building blocks for analyzing and understanding discrete-time systems.

# ### Objectives

# * To understand the basic concepts of elementary discrete-time signals.
# * To generate the unit sample, unit step, and unit ramp signals.
# * To implement these signals using **MATLAB/Python**.
# * To plot and observe the characteristics of each signal.
# * To understand the applications of these basic signals in digital signal processing.
