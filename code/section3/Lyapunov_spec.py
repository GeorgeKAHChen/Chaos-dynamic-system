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
Delta_t = 0.01
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
"""
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
"""
#=========================================










def main():
    """         
    curr_states = states()
    Lyapunov_spec = []
    e = np.array([0 for n in range(len(initial_value))])
    for kase in range(0, len(curr_states)):
        print(kase, len(curr_states), end = "\r")
        Jacobian = Jf(curr_states[kase])
        eig_val, eig_vec = np.linalg.eig(Jacobian)
        for ttl in range(0, len(initial_value)):
            e[ttl] += np.log(np.abs(np.real(eig_val[ttl])))
        Lyapunov_spec.append(np.power(e, 1/(kase+1)))
    print()
    print(Lyapunov_spec)
    print()
    val_x = x_axis
    plt.grid(True)
    for i in range(0, len(initial_value)):
        val = []
        for j in range(0, len(Lyapunov_spec)):
            val.append(Lyapunov_spec[j][i])
        plt.plot(val_x, val, COLOR_LOOP[i % len(COLOR_LOOP)])

    plt.show()  
    
    """


    curr_states = states()
    output_vals = [[0 for n in range((len(initial_value)))]]
    orth_mat = np.eye(len(initial_value))
    for kase in range(0, len(curr_states) - 1):
        Jacobian = np.matrix(Jf(curr_states[kase]))
        orth_mat = np.matrix(linalg.orth(np.matrix(Jacobian * np.matrix(orth_mat))))
        new_output = copy.deepcopy(output_vals[len(output_vals) - 1])
        for i in range(0, len(initial_value)):
            norm = np.linalg.norm(orth_mat[:, i])
            new_output[i] += ((new_output[i] * kase) + np.log(norm)) / (kase + 1)
        output_vals.append(new_output)


    output_vals = np.matrix(output_vals)
    val_x = x_axis
    plt.grid(True)
    for i in range(0, len(initial_value)):
        val = np.array(output_vals[:, i].reshape(-1).reshape(-1))
        print(val[0])
        print(val_x)
        plt.plot(val_x, val[0], COLOR_LOOP[i % len(COLOR_LOOP)])

    plt.show()  
    
    

if __name__ == '__main__':
    main()
