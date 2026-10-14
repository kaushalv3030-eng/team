import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the ODE: dy/dt = -k * y
def model(y, t, k):
    return -k * y

# Initial condition
y0 = 5.0

# Time points
t = np.linspace(0, 20, 100)

# Solve the ODE
k = 0.1
y = odeint(model, y0, t, args=(k,))

# Plot the result
plt.figure(figsize=(8,4))
plt.plot(t, y)
plt.xlabel('Time t')
plt.ylabel('y(t)')
plt.title('Exponential Decay: dy/dt = -0.1 y')
plt.grid(True)
plt.show()
