import numpy as np
import matplotlib.pyplot as plt

def euler_method(f, y0, t0, tf, h):
    """
    Implements the Euler method for solving ODEs.
    
    Parameters:
        f: The function f(t, y) representing the ODE dy/dt = f(t, y).
        y0: Initial value of y at t0.
        t0: Initial time.
        tf: Final time.
        h: Step size.
    
    Returns:
        t_values: Array of time points.
        y_values: Array of solution values at each time point.
    """
    t_values = np.arange(t0, tf + h, h)
    y_values = np.zeros(len(t_values))
    
    y_values[0] = y0
    
    for i in range(1, len(t_values)):
        y_values[i] = y_values[i-1] + h * f(t_values[i-1], y_values[i-1])
    
    return t_values, y_values

# Example usage:
# Solve dy/dt = -2y with y(0) = 1 over the interval [0, 5] with step size 0.1.

def f(t, y):
    return -2 * y

y0 = 1.0
t0 = 0.0
tf = 5.0
h = 0.1

t_values, y_values = euler_method(f, y0, t0, tf, h)

# Plotting the solution
plt.plot(t_values, y_values, label='Euler Method')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Solution of dy/dt = -2y using Euler Method')
plt.legend()
plt.grid(True)
plt.show()
