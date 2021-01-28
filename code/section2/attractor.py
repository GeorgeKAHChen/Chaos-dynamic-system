import numpy as np
import matplotlib.pyplot as plt
import random
import Init
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
interval_para = [0, 1.249]
#interval_para = [1, 4]
#distance_para = 0.000005
distance_para = 0.0001
distance_y = 0.001
memory_dimension = 0

Block_min_max = True
min_max_boundary = [-2.5, 2.5]

def f(x, parameter):
    #return 2 * x * (1 - x)
    #return (3*x - x*x*x)/2
    #return 3.3 * x * (1-x)
    #return parameter * x * (1-x)
    #a, b = 2, -0.3
    #a, b = 1.28, -0.3
    #a, b = 0, 0.4
    return [parameter - x[0] * x[0] + 0.4 * x[1], x[0]]


def main():
    parameter = interval_para[0]
    y_min =  999999999
    y_max = -999999999
    para_list = [parameter]
    list_rem = 0
    fx_list = [[]]
    while 1:
        print(parameter, interval_para[1], end = "\r")
        #x = [random.random(), random.random()]
        x = [0.1, 0.1]
        fx = f(x, parameter)
        #print("0 " + str(fx))
        for i in range(0, total_iteration_time):
            #plt.plot([x, fx], [fx, fx], color[kase])
            x = fx
            fx = f(x, parameter)
            if i > record_time:
                if not Block_min_max:
                    if y_min > fx[memory_dimension]:
                        y_min = fx[memory_dimension]
                    if y_max < fx[memory_dimension]:
                        y_max = fx[memory_dimension]
                fx_list[list_rem].append(fx[memory_dimension])
        
        parameter += distance_para
        if parameter > interval_para[1]:
            break
        para_list.append(parameter)
        fx_list.append([])
        list_rem += 1
    
    #Init.ArrOutput(fx_list, Mode = 0)
    print()
    #print(y_max, y_min)
    #print(para_list, int((y_max - y_min) / distance_y) + 1)
    if Block_min_max:
        y_min = min_max_boundary[0]
        y_max = min_max_boundary[1]
    img = [[255 for n in range(len(para_list))] for n in range(int((y_max - y_min) / distance_y) + 1)]
    print(len(para_list), len(fx_list))
    for i in range(0, len(para_list) - 2):
        #print(i, len(para_list), end = "\r")
        for j in range(0, len(fx_list[i]) - 1):
            #print(j, end = "\r")
            if fx_list[i][j] > y_max or fx_list[i][j] < y_min:
                continue
            loc_y = int((y_max - fx_list[i][j])/distance_y)
            loc_x = i
            img[loc_y][loc_x] = 0
        #print()
    img = np.float32(img)
    #print()
    Init.ImageIO(file_dir = "./img.png", img = np.float32(img), io = "o", mode = "grey", backend = "opencv")


if __name__ == '__main__':
    main()
