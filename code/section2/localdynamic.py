import numpy as np
import matplotlib.pyplot as plt
import math
import copy
import Init


DATA_OUTPUT = True
OUTPUT_LOCATION = "./output"

MODE = "S"      
"""
C: Analysis the convergence and disconvergence in circle neighborhood
S: Analysis every point in square is convergence or disconvergence
"""
#============================================
center = [-0.6, -0.6]
epsilon = 0.1
interval_x = [-2.5, 2.5]
interval_y = [-2.5, 2.5]
distance = 0.001
iteration_time = 100
boundary = [-10, 10, -10, 10]
iteration_color_loop = ["r", "g", "b", "c", "m"]
point_size = 0.1
def f(group_x):
    #print(group_x[0], group_x[1], -group_x[0] * group_x[0] + 0.4 * group_x[1], group_x[0])
    return [1.4 - group_x[0] * group_x[0] - 0.3 * group_x[1], group_x[0]]
#============================================







def neighborhood(center = [1, 1, 1], epsilon = 1, distance = 0.25):
    x = np.linspace(-epsilon, epsilon, int(2 * epsilon / distance) + 1)
    epsilon_squ = epsilon * epsilon
    
    vec_x = []
    for kase in range(0, len(center) - 1):
        vec_x.append(x)
    
    vec_stack = []
    value_stack = []
    for i in range(0, len(vec_x[0])):
        vec_stack.append([vec_x[0][i]])
        value_stack.append(vec_x[0][i] * vec_x[0][i])

    return_vec = []
    mark_stack = 0
    if len(center) !=2:
        while 1:
            new_mark = len(vec_stack[mark_stack])
            for i in range(0, len(vec_x[new_mark])):
                new_value = vec_x[new_mark][i] * vec_x[new_mark][i] + value_stack[mark_stack]
                if new_value <= epsilon_squ + 0.00000000001:
                    new_vec = copy.deepcopy(vec_stack[mark_stack])
                    new_vec.append(vec_x[new_mark][i])
                    if len(new_vec) == len(center) - 1:
                        return_vec.append(new_vec)
                    else:
                        vec_stack.append(new_vec)
                        value_stack.append(new_value)
            mark_stack += 1
            if mark_stack >= len(vec_stack):
                break
    else:
        return_vec = vec_stack


    ttl_kase = len(return_vec)
    for i in range(0, ttl_kase):
        #print(return_vec[i])
        new_vec = copy.deepcopy(return_vec[i])
        final_z = epsilon_squ
        for j in range(0, len(new_vec)):
            final_z -= new_vec[j] * new_vec[j]
        #print(final_z)
        final_z = math.sqrt(final_z)
        return_vec[i].append(final_z)
        if not final_z < 0.00000000001 and final_z > -0.00000000001:
            new_vec.append(-final_z)
            return_vec.append(new_vec)
    
    for j in range(0, len(center)):
        for i in range(0, len(return_vec)):
            return_vec[i][j] += center[j]
    
    return return_vec


def square(interval_x, interval_y):
    size_x = int((interval_x[1] - interval_x[0]) / distance) + 1
    size_y = int((interval_y[1] - interval_y[0]) / distance) + 1
    x_all = np.linspace(interval_x[0], interval_x[1], size_x)
    y_all = np.linspace(interval_x[0], interval_x[1], size_y)
    return_vec = []
    return_code = []
    for i in range(0, len(x_all)):
        for j in range(0, len(y_all)):
            return_vec.append([x_all[i], y_all[j]])
            return_code.append([i, j])
    return return_vec, return_code, size_x, size_y






def main():
    if MODE == "C":
        int_x = neighborhood(center, epsilon, distance)
        int_y = []
        int_y.append(int_x)
        #print(int_x)
        global DATA_OUTPUT
        for kase in range(0, iteration_time):
            print(kase , iteration_time)
            #print(int_y)
            curr_x = int_y[kase]
            curr_y = []
            for iteration in range(0, len(curr_x)):
                curr_y.append(f(curr_x[iteration]))
            int_y.append(curr_y)
        #print(int_y)
        if len(center) == 2:
            plt.figure(figsize=(9, 9)) 
            plt.grid(True)
            for i in range(0, len(int_y)):
                print(i, len(int_y))
                for j in range(0, len(int_y[i])):
                    if i == 0:
                        plt.scatter(int_y[i][j][0], int_y[i][j][1], s = point_size, color = "black")
                    else:
                        plt.scatter(int_y[i][j][0], int_y[i][j][1], s = point_size, color = iteration_color[i - 1])
            
            plt.show()
            plt.savefig('Output.png')
        elif len(center) == 3:
            plt.figure(figsize=(9, 9)) 
            plt.grid(True)
            ax = plt.axes(projection='3d')
            for i in range(0, len(int_y)):
                print(i, len(int_y))
                for j in range(0, len(int_y[i])):
                    if i == 0:
                        ax.scatter(int_y[i][j][0], int_y[i][j][1], int_y[i][j][2], s = point_size, color = "black")
                    else:
                        ax.scatter(int_y[i][j][0], int_y[i][j][1], int_y[i][j][2], s = point_size, color = iteration_color[i - 1])
            
            plt.show()
            plt.savefig('Output.png')

        else:
            print("The point file will save in '" + OUTPUT_LOCATION + "'.")
            DATA_OUTPUT = True

        if DATA_OUTPUT:
            Output_String = ""
            for j in range(0, len(int_y[i])):
                for i in range(0, len(int_y)):
                    for k in range(0, len(int_y[i][j])):
                        Output_String += str(int_y[i][j][k])
                        Output_String += " "
                    Output_String += " "
                Output_String += "\n"
            FileName = OUTPUT_LOCATION
            File = open(FileName, "w")
            File.write(Output_String)
            File.close()

    else:
        int_x, img_x, size_x, size_y = square(interval_x, interval_y)
        img = [[0 for n in range(size_x)] for n in range(size_y)]

        #mono = [0 for n in range(len(int_x))]
        for i in range(0, len(int_x)):
            print(i, len(int_x), end = "\r")
            int_y = int_x[i]
            curr_mono = 0
            for kase in range(0, iteration_time):
                int_y = f(int_y)
                if int_y[0] < boundary[0] or int_y[0] > boundary[1]:
                    if int_y[1] < boundary[2] or int_y[1] > boundary[3]:
                        curr_mono = 1
                        break
            if curr_mono:
                img[size_y - img_x[i][1] - 1][img_x[i][0]] = 0
            else:
                img[size_y - img_x[i][1] - 1][img_x[i][0]] = 255
        print()
        Init.ImageIO(file_dir = "./Output.png", img = np.float32(img), io = "o", mode = "grey", backend = "opencv")

if __name__ == '__main__':
    main()
