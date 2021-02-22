import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import random


COLOR_LOOP = ["r", "g", "b", "c", "m"]

#=========================================
#
#   Lorenz model 
#
#
#=========================================
"""
#rho = 28.0
#sigma = 10.0
#beta = 8.0 / 3.0

rho = 45.92
sigma = 4
beta = 10


initial_value = [1.0, 1.0, 1.0]
x_axis = np.arange(0.0, 500.0, 0.001)

def f(state, t):
    x, y, z = state
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z

def Jf(state):
    x, y, z = state
    return np.matrix([[-sigma, sigma, 0], [(rho - z), -1, -x], [y, x, -beta]])

def states():
    return odeint(f, initial_value, x_axis)

"""






#=========================================
#
#   Henon's model
#
#
#=========================================
"""
iteration_total = 1000
initial_value = [random.random(), random.random()]
x_axis = np.arange(0, iteration_total + 1, 1)
a = 1.4
b = 0.3
def f(int_x):
    x = int_x[0]
    y = int_x[1]
    return [1 - a * x * x + b * y, x]

def Jf(int_x):
    x = int_x[0]
    y = int_x[1]
    return np.matrix([[-2*a*x, b], [1, 0]])

def states():
    states = [initial_value]
    for i in range(0, iteration_total):
        states.append(f(states[len(states) - 1]))
    return states
"""


#=========================================
#
#   Logistic model
#
#
#=========================================

iteration_total = 1000
initial_value = [random.random()]
x_axis = np.arange(0, iteration_total + 1, 1)
a = 4
def f(int_x):
    x = int_x[0]
    return [4 * x * (1 - x)]

def Jf(int_x):
    x = int_x[0]
    return np.matrix([4 - 8 * x])

def states():
    states = [initial_value]
    for i in range(0, iteration_total):
        states.append(f(states[len(states) - 1]))
    return states

#=========================================









def main():
    curr_states = states()
    matrix_eigen = []
    for kase in range(0, len(curr_states)):
        Jacobian = [Jf(curr_states[kase])]
        eig_val, _ = np.linalg.eig(Jacobian)
        eig_val = np.abs(np.real(eig_val))
        matrix_eigen.append(eig_val)

    curr_expo = matrix_eigen[0]
    Lyapunov_spec = [np.log(curr_expo)]
    last_expo = curr_expo
    for kase in range(1, len(curr_states)):
        print(kase, len(curr_states), end = "\r")
        curr_expo = np.power(matrix_eigen[kase], 1/(kase + 1))
        curr_expo = curr_expo * np.power(last_expo, kase/(kase + 1))
        Lyapunov_spec.append(np.log(curr_expo))
        last_expo = curr_expo

    val_x = x_axis
    plt.grid(True)
    for i in range(0, len(initial_value)):
        val = []
        for j in range(0, len(Lyapunov_spec)):
            val.append(Lyapunov_spec[j][0][i])
        plt.plot(val_x, val, COLOR_LOOP[i % len(COLOR_LOOP)])

    plt.show()           
    

if __name__ == '__main__':
    main()
