import numpy as np
import matplotlib.pyplot as plt
import random
import Init

total_iteration_time = 100
interval_para = [[-1.5, 0.6], [-1, 1]]
delta_para = 0.001
initial_val = [0, 0]
inf_val = 100

def f(x, parameter):
    val_x, val_y = x
    c_x, c_y = parameter
    return [val_x * val_x - val_y * val_y + c_x, 2 * val_x * val_y + c_y]


def main():
    para_x = np.arange(interval_para[0][0], interval_para[0][1], delta_para)
    para_y = np.arange(interval_para[1][0], interval_para[1][1], delta_para)
    img = [[0 for n in range(len(para_y))] for n in range(len(para_x))]
    for i in range(0, len(para_x)):
        for j in range(0, len(para_y)):
            print(i, j, len(para_x), len(para_y), end = "\r")
            x = initial_val
            for kase in range(0, total_iteration_time):
                x = f(x, [para_x[i], para_y[j]])
                if x[0] > inf_val or x[1] > inf_val or x[0] < -inf_val or x[1] < -inf_val:
                    img[i][j] = 255
                    break
    print()
    img = np.float32(img)
    #print()
    Init.ImageIO(file_dir = "./img.png", img = np.float32(img), io = "o", mode = "grey", backend = "opencv")


if __name__ == '__main__':
    main()
