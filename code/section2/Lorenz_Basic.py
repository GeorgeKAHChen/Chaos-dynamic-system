import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

SOLUTION = "xy"
"""
"3d" means simulate 3d Lorenz model identity
"zt" means simulate Lorenz model t-z orbit
"zm" means simulate Lorenz map with z 
"""
#=========================================
#Parameter set
rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0
"""
Lorenz model parameter
"""
state0 = [1.0, 1.0, 1.0]
#t = np.arange(0.0, 10000.0, 0.0001)
t = np.arange(0.0, 40.0, 0.001)
#=========================================




def f(state, t):
    x, y, z = state
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z


def main():
    states = odeint(f, state0, t)
    if SOLUTION == "3d":
        fig = plt.figure()
        ax = fig.gca(projection="3d")
        ax.plot(states[:, 0], states[:, 1], states[:, 2], color = "black")
        """
        ax.scatter(0, 0, 40, color = "r")
        ax.scatter(40, 0, 0, color = "g")
        
        X = np.arange(-20, 20, 1)
        Y = np.arange(-20, 20, 1)
        Z = np.array([[sigma - 1 for n in range(len(X))] for n in range(len(Y))])
        
        surf = ax.plot_surface(X, Y, Z)
        fig.colorbar(surf, shrink=0.5, aspect=5)
        """


    elif SOLUTION == "zt" or SOLUTION == "zm":
        states_z = states[:, 2]
        z_n = []
        i_set = []
        for i in range(1 ,len(states_z) - 1):
            if states_z[i] > states_z[i+1] and states_z[i] > states_z[i-1]:
                z_n.append(states_z[i])
                i_set.append(i)

        if SOLUTION == "zm":
            for i in range(0, len(z_n) - 1):
                print(i, len(z_n) - 2, end = "\r")
                plt.scatter(z_n[i], z_n[i + 1], color = "red", s = 0.5)
        if SOLUTION == "zt":
            #plt.plot(t, states[:, 0], color = "g")
            #plt.plot(t, states[:, 1], color = "r")
            plt.plot(t, states[:, 2], color = "b")
            for i in range(0, len(z_n)):
                plt.scatter(t[i_set[i]], z_n[i], color = "red", s = 3)
                #plt.plot([t[i_set[i]], t[i_set[i]]], [-20, 50], "c-", linewidth = 0.5)

        print()
    if SOLUTION == "xy":
        x = states[:, 0]
        y = states[:, 1]
        plt.plot(x, y)
        for i in range(0, len(x)):
            print(i, len(x), end = "\r")
            plt.scatter(x[i], y[i], color = "red", s = 0.1)
        print()
    plt.draw()
    plt.show()






if __name__ == '__main__':
    main()
