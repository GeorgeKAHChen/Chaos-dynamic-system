import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import random
from scipy import linalg
import copy

COLOR_LOOP = ["r", "b", "g", "c", "m"]

interval_x = [[0, 1], [0, 1]]
delta_x = 0.01
image = "../../figure/CHAOS_1.png"
iter_time = 10
mark_sign = [0, 0.5]

def f(input_val):
    x, y = input_val
    if y <= 0.5:
        return [x / 3, 2 * y]
    else:
        return [x / 3 + 2 / 3, 2 * y - 1]





def gene_val(interval_x, delta_x):
    x_vals = []
    for kase in range(len(interval_x)):
        tmp = np.linspace(interval_x[kase][0], interval_x[kase][1], int(np.abs(interval_x[kase][0]-interval_x[kase][1])/delta_x))
        new_group = []
        if len(x_vals) == 0:
            for i in range(0, len(tmp)):
                new_group.append([tmp[i]])
            x_vals = copy.deepcopy(new_group)
        else:
            for i in range(0, len(x_vals)):
                for j in range(0, len(tmp)):
                    new_group.append(x_vals[i] + [tmp[j]])
            x_vals = copy.deepcopy(new_group)
    return x_vals


def plot_img(x_vals, x_mark):
    for i in range(0, len(x_vals)):
        plt.scatter(x_vals[i][0], x_vals[i][1], color = x_mark[i], s = 0.1)
    plt.show()
    input("press Enter key to continue ")


def main():
    
    x_vals = gene_val(interval_x, delta_x)
    x_mark = []
    for i in range(0, len(x_vals)):
        if x_vals[i][mark_sign[0]] < mark_sign[1]:
            x_mark.append(["r"])
        else:
            x_mark.append(["b"])
    plot_img(x_vals, x_mark)
    for kase in range(0, iter_time):
        new_x = []
        for i in range(0, len(x_vals)):
            new_x.append(f(x_vals[i]))
        x_vals = copy.deepcopy(new_x)
        plot_img(x_vals, x_mark)


    




if __name__ == '__main__':
    main()