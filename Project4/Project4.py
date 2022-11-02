#CST-305 Modeling and Simulation - Project 4 - Degradation of Data Integrity 
#Dylan Dorough and Haley Hansen 

import matplotlib.pyplot as plt
import numpy as np
import time

#function that prints running time of program
start = time.time()
print("The total running time is: ")
end = time.time()
print(end - start)

# Create the vectors X and Y
x = np.array(range(100))
y = np.exp((-0.05)*x)

# Create the plot
plt.plot(x, y)

plt.title('Data Loss Over Time')
plt.xlabel('time')
plt.ylabel('y(t)')
# Show the plot
plt.show()
