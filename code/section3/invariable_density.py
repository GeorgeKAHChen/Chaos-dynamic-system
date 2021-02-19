import Init
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
import random 

OUTPUT = True
FIGURE = True
INPUT = False
SAVE_FILENAME = "SaveArr_main"
#============================================
parameter_interval = [1, 4]
delta_parameter = 0.001
distribution_interval = [0, 1]
delta_distribution = 0.01

#delta_parameter = 0.01
#delta_distribution = 0.1

total_iteration = 60000
mark_iteration = 10000

#iteration_color_loop = ["r", "g", "b", "c", "m"]

def f(group_x, para):
    return [para * group_x[0] * (1 - group_x[0])]
#============================================

def main():
    if not INPUT:
        para = parameter_interval[0]
        #sub_stats_table = [0 for n in range(int((distribution_interval[1] - distribution_interval[0])/delta_distribution))]

        piece_point = np.linspace(distribution_interval[0], distribution_interval[1], int((distribution_interval[1] - distribution_interval[0])/delta_distribution) + 1)
        point_table = []
        for i in range(0, len(piece_point) - 1):
            point_table.append((piece_point[i] + piece_point[i+1]) / 2)
        
        main_stats_table = []
        para_table = []    
        
        while 1:
            val_x = random.random()
            val_x = val_x * (distribution_interval[1] - distribution_interval[0]) + distribution_interval[0]
            #curr_stats_table = deepcopy(sub_stats_table)
            curr_stats_table = [0 for n in range(int((distribution_interval[1] - distribution_interval[0])/delta_distribution))]
            para_table.append(para)
            print(para, end = "\r")
            x = [val_x]
            for kase in range(0, total_iteration):
                #print(str(para) + ":\t" + str(kase) + "/" + str(total_iteration), end = "\r")
                x = f(x, para)
                if kase >= mark_iteration:
                    try:
                        curr_stats_table[int((x[0] - distribution_interval[0]) / delta_distribution) + 1] += 1
                    except:
                        pass
            #print()
            for i in range(0, len(curr_stats_table)):
                curr_stats_table[i] = curr_stats_table[i] / (total_iteration - mark_iteration)
            main_stats_table.append(curr_stats_table)

            para += delta_parameter
            if para > parameter_interval[1]:
                break
        print()
        if OUTPUT == True:
            print("File output")
            String = str(len(point_table)) + " " + str(len(para_table)) + "\n"
            for i in range(0, len(point_table)):
                String += str(point_table[i])
                String += " "
            String += "\n"

            for i in range(0, len(para_table)):
                String += str(para_table[i])
                String += " "
            String += "\n"

            for i in range(0, len(main_stats_table)):
                for j in range(0, len(main_stats_table[i])):
                    String += str(main_stats_table[i][j])
                    String += " "
                String += "\n"
            FileName = "SaveArr" + str(Init.GetTime())
            File = open(FileName, "a")
            File.write(String)
            File.close()

    else:
        File = open(SAVE_FILENAME, "r")
        line = File.readline()
        val = Init.FileReadLine(line, mode = "int")
        point_size, para_size = val[0], val[1]
        line = File.readline()
        point_table = Init.FileReadLine(line, mode = "float")
        line = File.readline()
        para_table = Init.FileReadLine(line, mode = "float")
        main_stats_table = []
        print(len(point_table), len(para_table))
        kase = 0 
        while 1:
            kase += 1 
            print(kase, para_size, end = "\r")
            line = File.readline()
            if not line:
                break
            main_stats_table.append(Init.FileReadLine(line, mode = "float"))
        


    if FIGURE == True:
        point_table = np.array(point_table)
        para_table = np.array(para_table)
        point = np.array([point_table for n in range(len(para_table))]).reshape(-1)
        para = []
        for i in range(0, len(para_table)):
            for j in range(0, len(point_table)):
                para.append(para_table[i])
        para = np.array(para)
        main_stats_table = np.array(main_stats_table).reshape(-1)
        print(len(point), len(para), len(main_stats_table))
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.bar3d(para, point, np.zeros(len(main_stats_table)), delta_parameter, delta_distribution, main_stats_table)#,cmap='viridis', edgecolor='none')
        plt.show()




if __name__ == '__main__':
    main()
