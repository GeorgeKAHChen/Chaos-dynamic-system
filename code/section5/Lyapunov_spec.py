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
"""
rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0

#rho = 45.92
#sigma = 4
#beta = 10

#Delta_t = 0.01     #For test
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
"""





#=========================================
#
#   Henon's model
#
#
#=========================================


iteration_total = 50000
#iteration_total = 50
initial_value = [random.random()/10, random.random()/10]
x_axis = np.arange(0, iteration_total + 1, 1)
a = 1.4
b = 0.3
def f(int_x):
    x = int_x[0]
    y = int_x[1]
    #return [1 - a * x * x + b * y, x]
    return [a -  x * x + b * y, x]
    #return [1 - a * x * x + y, b * x]

def Jf(int_x):
    x = int_x[0]
    y = int_x[1]
    #return np.matrix([[-2*x+1, b], [1, 1]])
    return np.matrix([[-2*x, 1], [b, 0]])

def states():
    states = [initial_value]
    for i in range(0, iteration_total):
        states.append(f(states[len(states) - 1]))
    #print(states)
    return states






#=========================================
#
#   Logistic model
#
#
#=========================================
"""
iteration_total = 100000
initial_value = [random.random()]
x_axis = np.arange(0, iteration_total + 1, 1)
a = 3.95
def f(int_x):
    x = int_x[0]
    return [a * x * (1 - x)]

def Jf(int_x):
    x = int_x[0]
    return np.matrix([a - 2 * a * x])

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
b = 0.2
c = 5.7


Delta_t = 0.01
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



#=========================================
#
#   4-dim system
#
#
#=========================================
"""
Delta_t = 0.001
initial_value = [random.random(), random.random(), random.random(), random.random()]
x_axis = np.arange(0.0, 50.0, Delta_t)

def f(state, t):
    x, y, z, w = state
    return -y-z, x+0.25*y+w, 3+x*y, -0.5*z+0.05*w

def Jf(state):
    x, y, z, w = state
    return np.matrix([[1        , -Delta_t      , -Delta_t      , 0             ],
                      [Delta_t  , 1+0.25*Delta_t, 0             , Delta_t       ],
                      [z*Delta_t, 0             , 1+x*Delta_t   ,0              ],
                      [0        , 0             , -0.5*Delta_t  , 1+0.05*Delta_t]])


def states():
    return odeint(f, initial_value, x_axis)
"""



#=========================================
#
#   Ikeda map 
#
#
#=========================================

"""

iteration_total = 50000
#iteration_total = 50
initial_value = [random.random(), random.random()]
x_axis = np.arange(0, iteration_total + 1, 1)
para_c1 = 0.4
para_c2 = 0.9
para_c3 = 6
para_r = 1

def f(int_x):
    x = int_x[0]
    y = int_x[1]
    tau = para_c1 - para_c3 / (1 + x*x + y*y)
    return [para_r + para_c2 * (x * np.cos(tau) - y * np.sin(tau)),
                     para_c2 * (x * np.sin(tau) + y * cos(tau))]


def Jf(int_x):
    x = int_x[0]
    y = int_x[1]
    tmp = 1 / (1 + x*x + y*y)
    tau = para_c1 - para_c3 * tmp
    dtau_dx = 2 * para_c3 * x * tmp * tmp
    dtau_dx = 2 * para_c3 * y * tmp * tmp
    sin_tau = np.sin(tau)
    cos_tau = np.cos(tau)
    return np.matrix([para_c2 * cos_tau - [para_c2*x*sin_tau + para_c2*y*cos_tau] * dtau_dx, ]
        )

def states():
    states = [initial_value]
    for i in range(0, iteration_total):
        states.append(f(states[len(states) - 1]))
    #print(states)
    return states

"""





"""
#   Main function: Lyapunov Spec
"""
def Gram_Schmidt(input_matrix):
    #print(input_matrix)
    input_matrix = np.array(input_matrix)
    input_matrix = np.transpose(input_matrix)
    size1 = np.size(input_matrix[:, 0])
    size2 = np.size(input_matrix[0, :])
    if size1 != size2:
        ValueError("Input matrix in Gram_Schmidt must be a square.")
    squ_vals = []
    return_matrix = []
    for kase in range(0, size1):
        curr_mat = input_matrix[kase, :]
        final_mat = input_matrix[kase, :]
        for i in range(0, kase):
            final_mat -= (sum(return_matrix[i] * curr_mat) / squ_vals[i]) * return_matrix[i]
        return_matrix.append(final_mat)
        squ_vals.append(sum(final_mat * final_mat))
    
    final_mat = []
    for kase in range(0, size1):
        curr_vec = return_matrix[kase]
        curr_vec /= np.linalg.norm(curr_vec)
        final_mat.append(curr_vec)
    #print(np.matrix(np.transpose(final_mat)))
    return np.matrix(np.transpose(final_mat))








def main():
    curr_states = states()
    output_vals = [[0 for n in range((len(initial_value)))]]
    orth_mat = np.eye(len(initial_value))
    for kase in range(0, len(curr_states) - 1):
        if kase % 1000 == 0:
            print(kase, len(curr_states) - 2, end = "\r")
        Jacobian = np.matrix(Jf(curr_states[kase]))
        tmp = np.matrix(Jacobian) * np.matrix(orth_mat)
        #orth_mat = np.matrix(linalg.orth(tmp))
        orth_mat = Gram_Schmidt(tmp)
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

    print()
    output_str = "Output Vals\nLyapunov vals: \t"
    output_str += str(output_vals[len(output_vals) - 1])
    output_str += "\n sum: " + str(sum_val[len(sum_val) - 1])
    print(output_str)
    plt.show()  
    
    

if __name__ == '__main__':
    main()
