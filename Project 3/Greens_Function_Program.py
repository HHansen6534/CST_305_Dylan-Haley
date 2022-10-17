# Dylan Dorough and Haley Hansen
# CST-305
# Professor Citro
# Project 3: Greens Function

# import numpy, math, and matplotlib

from numpy import *
import math
import matplotlib.pyplot as plt
from datetime import datetime

#start counting running time
start = datetime.now()

a = 0
for i in range (1000):
    a += (i**100)
#stop counting
end = datetime.now()

td = (end - start).total_seconds() * 10**3
                 # print running time to the terminal
print(f"The time of execution is : {td:.03f}ms")

# Define t to be solved between -50 and 50
t = linspace(-50, 50)
a = (4*exp(-t))+(2*t*exp(-t))+2*t-4
b = (t**2)+2*cos(t)-2
c = 4*exp(-t)+2*t*exp(-t)
d = 2*(cos(t))

# Create a new plot figure
figure, axis = plt.subplots(2, 2)

# Plot each equation on a different plot but in the same window
# Equation a
axis[0, 0].plot(t, a, 'b')
axis[0, 0].set_ylim([-50, 50])
axis[0, 0].set_title('Problem 1 Solved')
# Equation b
axis[0, 1].plot(t, b, 'b')
axis[0, 1].set_ylim([-50, 50])
axis[0, 1].set_title('Problem 2 Solved')
# Equation c
axis[1, 0].plot(t, c, 'b')
axis[1, 0].set_ylim([-50, 50])
axis[1, 0].set_title('Problem 1 Homogeneous')
# Equation d
axis[1, 1].plot(t, d, 'b')
axis[1, 1].set_ylim([-50, 50])
axis[1, 1].set_title('Problem 2 Homogeneous')

# show final plot
plt.show()




