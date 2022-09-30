# Dylan Dorough and Haley Hansen
# CST-305
# Professor Citro
# Project 2: RK4 with Python


# initial conditions
y0 = 5
x0 = 1
steps = 5
e = 2.71828183


# defining the equation provided
def f(x, y):
    return y/((e**x)-1)


# RK-4 function
def rk4(x0, y0, n):
    # Defining the step size
    h = 0.02

    print('---------SOLUTION---------')
    print('  x0      y0      yn      ')
    print('--------------------------')
    # Loop that will complete RK4 calculations to the number of steps defined above
    for i in range(n):
        # K1 formula
        k1 = (f(x0, y0))
        # K2 formula
        k2 = (f((x0 + (h/2)), (y0 + (h / 2) * k1)))
        # K3 formula
        k3 = (f((x0 + h / 2), (y0 + (h / 2) * k2)))
        # K4 formula
        k4 = (f((x0 + h), (y0 + h * k3)))
        # Solver for yn
        k = (h/6) * (k1 + 2 * k2 + 2 * k3 + k4)
        yn = y0 + k
        print('%.4f\t%.4f\t%.4f' % (x0, y0, yn))
        print('-------------------------')
        y0 = yn
        x0 = x0 + h


# Call RK4 function
rk4(x0, y0, steps)
