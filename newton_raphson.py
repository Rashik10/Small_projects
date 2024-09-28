import numpy as np
import matplotlib.pyplot as plt

def newton_raphson(func, deriv, x0, tolerance=1e-6, max_iterations=100):
    """
    Implements the Newton-Raphson method to find the root of a given function.
    
    Parameters:
        func: The function for which we are finding the root.
        deriv: The derivative of the function.
        x0: Initial guess for the root.
        tolerance: The tolerance for the root (default is 1e-6).
        max_iterations: The maximum number of iterations (default is 100).
    
    Returns:
        A value which is the estimated root of the function.
    """
    x_n = x0
    iterations = [x_n]  # List to store the iterates for plotting

    for n in range(max_iterations):
        fx_n = func(x_n)
        f_prime_x_n = deriv(x_n)
        
        if f_prime_x_n == 0:
            print("Zero derivative. No solution found.")
            return None
        
        x_n1 = x_n - fx_n / f_prime_x_n
        iterations.append(x_n1)
        
        if abs(x_n1 - x_n) < tolerance:
            print(f"Found solution after {n+1} iterations.")
            plot_newton_raphson(func, iterations)
            return x_n1
        
        x_n = x_n1
    
    print("Exceeded maximum iterations. No solution found.")
    plot_newton_raphson(func, iterations)
    return None

def plot_newton_raphson(func, iterations):
    """
    Plots the function and the iterations of the Newton-Raphson method.
    
    Parameters:
        func: The function for which the root is being found.
        iterations: A list of the iterates (approximations) from the Newton-Raphson method.
    """
    x_values = np.linspace(min(iterations)-1, max(iterations)+1, 400)
    y_values = func(x_values)

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label='f(x)')
    plt.axhline(0, color='black', linewidth=0.5)
    
    for i in range(1, len(iterations)):
        x_n = iterations[i-1]
        x_n1 = iterations[i]
        plt.plot([x_n, x_n], [0, func(x_n)], color='red', linestyle='--')
        plt.plot([x_n, x_n1], [func(x_n), 0], color='blue', linestyle='--')
    
    plt.scatter(iterations, [func(x) for x in iterations], color='green', zorder=5)
    plt.plot(iterations, [func(x) for x in iterations], color='green', linestyle='-', marker='o', label='Iterations')
    
    plt.title('Newton-Raphson Method')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage:
# Suppose we want to find the root of the equation f(x) = x^2 - 2.

def func(x):
    return x**2 - 2

def deriv(x):
    return 2*x

# Initial guess
x0 = 1.0

# Call Newton-Raphson method
root = newton_raphson(func, deriv, x0)

if root is not None:
    print(f"Root: {root}")
