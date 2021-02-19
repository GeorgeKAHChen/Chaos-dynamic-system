import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

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
t = np.arange(0.0, 40.0, 0.001)
iteration_total = 10


def f(state, t):
    x, y, z = state
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z

#=========================================





def main():
    states = odeint(f, state0, t)
    fig = plt.figure()
    #ax = fig.gca(projection="3d")
    #ax.plot(states[:, 0], states[:, 1], states[:, 2], color = "black")
    #fig.show()
    Lambda = []
    for kase in range(0, len(t)):


if __name__ == '__main__':
    main()
