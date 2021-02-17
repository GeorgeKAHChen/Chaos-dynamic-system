import Init
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
import random 

OUTPUT = True
FIGURE = False
#============================================
parameter_interval = [1, 4]
delta_parameter = 0.0001
distribution_interval = [0, 1]
delta_distribution = 0.001

total_iteration = 60000
mark_iteration = 10000

#iteration_color_loop = ["r", "g", "b", "c", "m"]

def f(group_x, para):
    return [para * group_x[0] * (1 - group_x[0])]
#============================================

def main():
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
        String = ""
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

    if FIGURE == True:
        point_table = np.array(point_table)
        para_table = np.array(para_table)
        """
        point = np.array([point_table for n in range(len(para_table))])
        para = []
        for i in range(0, len(para_table)):
            para.append([para_table[i] for n in range(len(point_table))])
        main_stats_table = np.array(main_stats_table)
        print(len(point_table), len(para_table), len(main_stats_table), len(main_stats_table[0]))
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        """
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
        #parapos, pointpos = np.meshgrid(para_table[:-1] + 0.5*delta_parameter, point_table[:-1] + 0.5*delta_distribution, indexing="ij")
        #parapos = parapos.ravel()
        #pointpos = pointpos.ravel()
        #valpos = 0
        #fig = plt.figure()
        #ax = fig.add_subplot(111, projection='3d')
        ax.bar3d(para, point, np.zeros(len(main_stats_table)), delta_parameter, delta_distribution, main_stats_table)#,cmap='viridis', edgecolor='none')
        #ax.bar3d(para_table, point_table, main_stats_table, parapos, pointpos, valpos)#,cmap='viridis', edgecolor='none')
        #ax.set_title('Surface plot')
        plt.show()



if __name__ == '__main__':
    main()