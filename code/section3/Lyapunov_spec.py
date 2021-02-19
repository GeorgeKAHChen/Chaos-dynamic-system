import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

COLOR_LOOP = ["r", "g", "b", "c", "m"]

#=========================================
#Parameter set
rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0
"""
Lorenz model parameter
"""
initial_value = [1.0, 1.0, 1.0]
#t = np.arange(0.0, 10000.0, 0.0001)
#t = np.arange(0.0, 40.0, 0.001)
t = np.arange(0.0, 2.0, 0.01)
#t = np.arange(0.0, 40.0, 1)
iteration_total = 10


def f(state, t):
    x, y, z = state
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z

def Jf(state):
    x, y, z = state
    return np.matrix([[-sigma, sigma, 0], [(rho - z), -1, -x], [y, x, -beta]])
#=========================================





def main():
    states = odeint(f, initial_value, t)
    fig = plt.figure()
    
    multi_Jf = Jf(states[0])
    eig_val, _ = np.linalg.eig(multi_Jf)
    Lyapunov_spec = [eig_val]

    for kase in range(1, len(t)):
        curr_Jf = Jf(states[kase])
        #print(curr_Jf)
        multi_Jf = curr_Jf * multi_Jf
        #print(multi_Jf)
        eig_val, _ = np.linalg.eig(multi_Jf)
        #print(eig_val)
        Lyapunov_spec.append(np.log(np.abs(eig_val)) / (1 + kase))

    plt.grid(True)
    for i in range(0, len(initial_value)):
        val = []
        for j in range(0, len(Lyapunov_spec)):
            val.append(Lyapunov_spec[j][i])
        plt.plot(t, val, COLOR_LOOP[i % len(COLOR_LOOP)])
    #ax = fig.gca(projection="3d")
    #ax.plot(states[:, 0], states[:, 1], states[:, 2], color = "black")

    plt.show()           


if __name__ == '__main__':
    main()
