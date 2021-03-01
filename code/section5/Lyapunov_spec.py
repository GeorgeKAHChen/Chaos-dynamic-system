import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import random
from scipy import linalg
import copy

COLOR_LOOP = ["r", "g", "b", "c", "m"]





#=========================================
#
#   Lorenz model 
#
#
#=========================================

rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0

#rho = 45.92
#sigma = 4
#beta = 10

#Delta_t = 0.001
#Delta_t = 1
Delta_t = 0.0001
initial_value = [1.0, 1.0, 1.0]
x_axis = np.arange(0.0, 50.0, Delta_t)

def f(state, t):
    x, y, z = state
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z

def Jf(state):
    x, y, z = state
    #return Delta_t * np.matrix([[-sigma, sigma, 0], [(rho - z), -1, -x], [y, x, -beta]]) + np.eye(3)
    return np.matrix([[1 - Delta_t * sigma,         Delta_t * sigma,        0], 
                      [Delta_t * (rho - z),         1 - Delta_t ,           -Delta_t * x], 
                      [Delta_t * y,                 Delta_t * x,            1 - Delta_t * beta]])


def states():
    return odeint(f, initial_value, x_axis)






#=========================================
#
#   Henon's model
#
#
#=========================================
"""
iteration_total = 50000
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
"""
iteration_total = 10000
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
"""
#=========================================





#=========================================
#
#   Rossler system
#
#
#=========================================
"""
a = 0.2
b = 0.3
c = 10


Delta_t = 0.0001
initial_value = [1.0, 1.0, 1.0]
x_axis = np.arange(0.0, 50.0, Delta_t)

def f(state, t):
    x, y, z = state
    return - y - z, x + a * y, b + z * (x - c)

def Jf(state):
    x, y, z = state
    #return Delta_t * np.matrix([[-sigma, sigma, 0], [(rho - z), -1, -x], [y, x, -beta]]) + np.eye(3)
    return np.matrix([[1,               -Delta_t,                   -Delta_t], 
                      [Delta_t,         a * Delta_t + 1 ,           0], 
                      [Delta_t * z,     0,                          (x - c) * Delta_t + 1]])


def states():
    return odeint(f, initial_value, x_axis)
"""





#=========================================
#
#   Duffing system
#
#
#=========================================
"""
val_alpha = 1
val_beta = 0.04
val_gamma = 1
val_delta = 0.1
val_omega = np.pi / 2


Delta_t = 0.0001
initial_value = [1.0, 1.0]
x_axis = np.arange(0.0, 50.0, Delta_t)

def f(state, t):
    x, y = state
    return y, val_gamma * np.cos(val_omega * t) - val_alpha * x - val_beta * x * x *x - val_delta * y

def Jf(state):
    x, y = state
    return np.matrix([[1,                                               -Delta_t                ], 
                      [(-val_alpha - 3 * val_beta * x * x) * Delta_t,   val_delta * Delta_t + 1 ]])


def states():
    return odeint(f, initial_value, x_axis)
"""






"""
#   Main function: Lyapunov Spec
"""


def main():
    curr_states = states()
    output_vals = [[0 for n in range((len(initial_value)))]]
    orth_mat = np.eye(len(initial_value))
    for kase in range(0, len(curr_states) - 1):
        Jacobian = np.matrix(Jf(curr_states[kase]))
        tmp = np.matrix(Jacobian) * np.matrix(orth_mat)
        orth_mat = np.matrix(linalg.orth(tmp))
        new_output = copy.deepcopy(output_vals[len(output_vals) - 1])
        for i in range(0, len(new_output)):
            norm = np.linalg.norm(tmp[:, i])
            new_output[i] = ((new_output[i] * (x_axis[kase] - x_axis[0])) + np.log(norm)) / (x_axis[kase + 1] - x_axis[0])
        output_vals.append(new_output)

    fig = plt.gcf()
    fig.set_size_inches(25, 3)
    output_vals = np.matrix(output_vals)
    plt.grid(True)
    for i in range(0, len(initial_value)):
        val = np.array(output_vals[:, i].reshape(-1).reshape(-1))
        plt.plot(x_axis, val[0], COLOR_LOOP[(i + 1) % len(COLOR_LOOP)])

    sum_val = []
    for i in range(0, len(output_vals)):
        sum_val.append(np.sum(output_vals[i][0]))
    plt.plot(x_axis, sum_val, COLOR_LOOP[0])

    output_str = "Output Vals\nLyapunov vals: \t"
    output_str += str(output_vals[len(output_vals) - 1])
    output_str += "\n sum: " + str(sum_val[len(sum_val) - 1])
    print(output_str)
    plt.show()  
    
    

if __name__ == '__main__':
    main()
