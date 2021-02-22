import numpy as np
import matplotlib.pyplot as plt
import random

COLOR_LOOP = ["r", "g", "b", "c", "m"]

#=========================================
iteration_total = 1000
initial_val = [random.random()]
#initial_val = [random.random(), random.random()]

"""
def f(int_x, prob):
    x = int_x[0]
    y = int_x[1]
    if prob < 1/3:
        return [x / 2, y / 2]
    elif prob < 2/3:
        return [(1 + x) / 2, y / 2]
    else:
        return [x / 2, (1 + y) / 2]
"""


def f(int_x, prob):
    if prob > 0.5:
        return [int_x[0] * 2 / 3]
    else:
        return [int_x[0] + (1 - int_x[0]) / 3]

#=========================================


def main():
    val_set = [initial_val]
    for i in range(0, iteration_total):
        val_set.append(f(val_set[len(val_set) - 1], random.random()))

    ret_x = np.arange(0, iteration_total + 1, 1)
    print(len(ret_x))
    for i in range(0, len(initial_val)):
        ret_y = []
        for j in range(0, len(val_set)):
            ret_y.append(val_set[j][i])
        plt.plot(ret_x, ret_y, COLOR_LOOP[i % len(COLOR_LOOP)])
    plt.show()
    return


if __name__ == '__main__':
    main()