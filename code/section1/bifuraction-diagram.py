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
interval_para = [3.825, 3.856]
#interval_para = [1, 4]
distance_para = 0.000005

distance_y = 0.0002

def f(x, parameter):
    #return 2 * x * (1 - x)
    #return (3*x - x*x*x)/2
    #return 3.3 * x * (1-x)
    return parameter * x * (1-x)


def main():
    parameter = interval_para[0]
    y_min =  999999999
    y_max = -999999999
    para_list = [parameter]
    list_rem = 0
    fx_list = [[]]
    while 1:
        print(parameter, interval_para[1], end = "\r")
        x = random.random()
        fx = f(x, parameter)
        #print("0 " + str(fx))
        for i in range(0, total_iteration_time):
            #plt.plot([x, fx], [fx, fx], color[kase])
            x = fx
            fx = f(x, parameter)
            if i > record_time:
                if y_min > fx:
                    y_min = fx
                if y_max < fx:
                    y_max = fx
                fx_list[list_rem].append(fx)
        
        parameter += distance_para
        if parameter > interval_para[1]:
            break
        para_list.append(parameter)
        fx_list.append([])
        list_rem += 1
    print()
    #print(y_max, y_min)
    #print(para_list, int((y_max - y_min) / distance_y) + 1)
    img = [[255 for n in range(len(para_list))] for n in range(int((y_max - y_min) / distance_y) + 1)]
    for i in range(0, len(para_list)):
        print(i, len(para_list), end = "\r")
        for j in range(0, len(fx_list[i])):
            loc_y = int((y_max - fx_list[i][j])/distance_y)
            loc_x = i
            img[loc_y][loc_x] = 0
    img = np.float32(img)
    print()
    Init.ImageIO(file_dir = "./img.png", img = np.float32(img), io = "o", mode = "grey", backend = "opencv")


if __name__ == '__main__':
    main()
