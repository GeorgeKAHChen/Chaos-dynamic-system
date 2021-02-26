import numpy as np
import Init

total_iteration_time = 1000
interval_para = [[-1.5, 0.6], [-1, 1]]
#delta_para = 0.0005
delta_para = 0.0001
initial_val = [0, 0]
inf_val = 100

def f(x, parameter):
    val_x, val_y = x
    c_x, c_y = parameter
    return [val_x * val_x - val_y * val_y + c_x, 2 * val_x * val_y + c_y]


def main():
    para_x = np.arange(interval_para[0][0], interval_para[0][1], delta_para)
    para_y = np.arange(interval_para[1][0], interval_para[1][1], delta_para)
    img = []
    for i in range(0, len(para_x)):
        img_x = []
        for j in range(0, len(para_y)):
            print(i, j, len(para_x), len(para_y), end = "\r")
            x = initial_val
            add_var = True
            for kase in range(0, total_iteration_time):
                x = f(x, [para_x[i], para_y[j]])
                if x[0] > inf_val or x[1] > inf_val or x[0] < -inf_val or x[1] < -inf_val:
                    img_x.append([255, 255, 255])
                    add_var = False
                    break
            if add_var:
                img_x.append([0, 0, 0])
        img.append(img_x)
    print()
    img = np.float32(img)
    #print()
    #print(img)
    Init.ImageIO(file_dir = "./img.png", img = np.float32(img), io = "o", mode = "grey", backend = "Pillow")


if __name__ == '__main__':
    main()
