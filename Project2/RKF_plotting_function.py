# Dylan Dorough and Haley Hansen
# CST-305
# Professor Citro
# Project 2: RK4 with Python Plotting function 

# Import libraries
import numpy as np
import scipy
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import time

# Start timer
start = time.time()

# initial conditions
ya = []
xa = []
y0 = 5
x0 = 1
steps = 2000


# Define function to be solved for RK4
def f(x, y):
    return y/((np.exp(x))-1)


# Define function for ODEINT
def model(y, x):
    return y/((np.exp(x))-1)


# Initialize the plot area
p = plt.figure()


# RK-4 function
def rk4(x0, y0, n):

    # Set step size
    h = 0.02

    # for loop the complete RK4 calculations based on number of steps defined
    for i in range(n):
        k1 = (f(x0, y0))
        k2 = (f((x0 + (h/2)), (y0 + (h / 2) * k1)))
        k3 = (f((x0 + h / 2), (y0 + (h / 2) * k2)))
        k4 = (f((x0 + h), (y0 + h * k3)))
        k = (h/6) * (k1 + 2 * k2 + 2 * k3 + k4)
        yn = y0 + k
        y0 = yn
        x0 = x0 + h

        # Add results to y and x array so they can be plotted
        ya.append(y0)
        xa.append(x0)
    # plotting each point in the arrays
    plt.plot(xa, ya, 'y-', linewidth=4, label='Rk4')


# Call RK4 function
rk4(x0, y0, steps)

# x points
x = np.linspace(1, 40, steps)

# solve ODE
y = odeint(model, y0, x)

# plot results
plt.plot(x, y, label='ODEINT')
plt.legend()
plt.show()

# record end time
end = time.time()

# print the difference between start
# and end time in milli. secs
print("The time of execution of above program is :",
      (end - start) * 10 ** 3, "ms")
