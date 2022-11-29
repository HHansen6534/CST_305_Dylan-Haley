# Dylan Dorough and Haley Hansen
# CST-305
# Professor Citro
# Project 6 Part 3

# import numpy, scipy, and matplotlib
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dy/dt (ODE)
# Frame rate and frame size are inversely related therefore the equation is k/p
# multiply p by 8 to convert from bit to bytes
def model(y, p, k):
    e = 2.71828183
    dydp = y/((e**p)-1)
    return dydp

# initial condition is 0
y0 = 0

# range of x axis (frame size), we would like to see from 100 to 1600 frame size
p = np.linspace(100, 1600)

# solve ODEs
# ODE 1: 3 GB
k = 3000000000
y1 = odeint(model, y0, p, args=(k,))
# ODE 2: 2 GB
k = 2000000000
y2 = odeint(model, y0, p, args=(k,))
# ODE 3: 1 GB
k = 1000000000
y3 = odeint(model, y0, p, args=(k,))
# ODE 4: 0.5 GB
k = 500000000
y4 = odeint(model, y0, p, args=(k,))
# ODE 5: 0.25 GB
k = 250000000
y5 = odeint(model, y0, p, args=(k,))
# ODE 6: 0.125 GB
k = 125000000
y6 = odeint(model, y0, p, args=(k,))

# plot results
f = plt.figure()
# Setting plot dimensions
f.set_figwidth(12)
f.set_figheight(4)
# Plotting each ODE
plt.plot(p, y1, 'r-', linewidth=2, label='3 GB')
plt.plot(p, y2, 'b-', linewidth=2, label='2 GB')
plt.plot(p, y3, 'g-', linewidth=2, label='1 GB')
plt.plot(p, y4, 'k-', linewidth=2, label='0.5 GB')
plt.plot(p, y5, 'y-', linewidth=2, label='0.25 GB')
plt.plot(p, y6, 'm-', linewidth=2, label='0.125 GB')
# Setting title and axis Labels
plt.title('Frames Transferred vs Frame Size')
plt.xlabel('Frame Size')
plt.ylabel('Frame Rate')
# Showing plot legend
plt.legend()
plt.show()
