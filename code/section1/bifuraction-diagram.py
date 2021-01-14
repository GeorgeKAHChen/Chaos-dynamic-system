import numpy as np
import matplotlib.pyplot as plt
import random

total_iteration_time = 110
record_time = 100
initial_value = random.random()
#interval_para = [1, 4.01]
distance_para = 0.01

total_iteration_time = 150
record_time = 100
initial_value = random.random()
interval_para = [3.825, 3.856]
distance_para = 0.0001


def f(x, parameter):
    #return 2 * x * (1 - x)
    #return (3*x - x*x*x)/2
    #return 3.3 * x * (1-x)
    return parameter * x * (1-x)


def main():
    int_x = np.linspace(interval_para[0], interval_para[1])
    parameter = interval_para[0]
    real_iteration = total_iteration_time
    change = False
    while parameter < interval_para[1]:
        print(parameter)
        x = initial_value
        fx = f(initial_value, parameter)
        #print("0 " + str(fx))
        for i in range(0, real_iteration):
            #plt.plot([x, fx], [fx, fx], color[kase])
            x = fx
            fx = f(x, parameter)
            if i > record_time:
                plt.scatter(parameter, fx, s = 1, color = "black")
                #print(str(i+1) + " " + str(parameter) + " " + str(fx))
        parameter += distance_para
        if parameter > 3.830 and parameter < 3.845:
            real_iteration = 120
        elif parameter >= 3.848:
            real_iteration = total_iteration_time
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
