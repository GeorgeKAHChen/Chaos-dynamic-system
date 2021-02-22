import numpy as np
import matplotlib.pyplot as plt
import random
import math


#total_iteration_time = 110
#record_time = 100
#initial_value = random.random()
#interval_para = [1, 4.01]
#distance_para = 0.01

total_iteration_time = 12000
record_time = 10000
#total_iteration_time = 120
#record_time = 100
#interval_para = [3.825, 3.856]
#interval_para = [0, 1.249]
interval_para = [3.99001, 4]
#interval_para = [1, 4]
#distance_para = 0.000005
distance_para = 0.0001
distance_y = 0.001
memory_dimension = 0


def f(x, parameter):
    #return 2 * x * (1 - x)
    #return (3*x - x*x*x)/2
    #return 3.3 * x * (1-x)
    return [parameter * x[0] * (1-x[0])]
    #a, b = 2, -0.3
    #a, b = 1.28, -0.3
    #a, b = 0, 0.4
    #return [parameter - x[0] * x[0] + 0.4 * x[1], x[0]]


def partical_f(x, parameter):
    return [parameter - 2 * parameter * x[0]]



def main():
    parameter = interval_para[0]
    para_list = [parameter]
    list_rem = 0
    fx_list = [0]
    while 1:
        print(parameter, interval_para[1], end = "\r")
        x = [0.1, 0.1]
        fx = f(x, parameter)
        for i in range(0, total_iteration_time):
            x = fx
            fx = f(x, parameter)
            pratical_fx = partical_f(x, parameter)
            #print(x, fx, pratical_fx)
            if i > record_time:
                if pratical_fx[memory_dimension] == 0:
                    continue
                fx_list[list_rem] += math.log(abs(pratical_fx[memory_dimension]))
        #print(parameter, fx_list[list_rem])
        fx_list[list_rem] /= total_iteration_time - record_time
        parameter += distance_para
        if parameter > interval_para[1]:
            break
        para_list.append(parameter)
        fx_list.append(0)
        list_rem += 1
    
    print()
    #print(para_list, fx_list)
    plt.plot(para_list, fx_list, "b")
    plt.show()


if __name__ == '__main__':
    main()
