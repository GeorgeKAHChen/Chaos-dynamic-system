import numpy as np
import matplotlib.pyplot as plt
import math

gnx = 1

#initial_value = [-2, -1.7, -0.3, 0, 0.1, 1.9]
#color = ["r-", "g-", "b-", "c-", "m-", "y-"]
#iteration_time = 10
#interval = [-2.2, 2.2]

#initial_value = [0.01, 0.2, 0.5, 0.95, 0.99]
#color = ["r-", "g-", "b-", "c-", "m-"]
#iteration_time = 10
#interval = [-0.1, 1.1]
"""
initial_value = [0.01, 0.4, 0.99]
color = ["r-", "g-", "b-"]
iteration_time = 1000
interval = [-0.1, 1.1]
"""

initial_value = [0.01, 0.2, 0.5, 0.95, 0.99]
color = ["r-", "g-", "b-", "c-", "m-"]
iteration_time = 1000
interval = [-0.001, 1.001]

"""
#initial_value = []#[0.01]#, 0.2, 0.5, 0.95, 0.99]
initial_value = [0.01, 0.25, 1/3, 0.5, 1]
color = ["r-", "g-", "b-", "c-", "m-"]
#initial_value = [1/3]#, 0.2, 0.5, 0.95, 0.99]
#color = ["r-"]#, "g-", "b-", "c-", "m-"]
iteration_time = 100
interval = [-0.001, 1.001]
"""
#initial_value = [(5-math.sqrt(5))/8]#, 0.25, 0.5, 0.75, (5+math.sqrt(5))/8]
#color = ["r-"]#, "g-", "b-", "c-", "m-"]
#initial_value = []#0.325, 0.25, 0.5, 0.75]
#color = ["r-", "g-", "b-", "c-"]
#iteration_time = 500
#interval = [-0.001, 1.001]
#initial_value = []#0.325, 0.25, 0.5, 0.75]
#color = ["r-", "g-", "b-", "c-"]
#iteration_time = 500
#interval = [-0.001, 1.001]

"""
initial_value = [0.2501, 0.25]#, 0.5, 0.75]
color = ["r-", "g-"]#, "b-", "c-"]
iteration_time = 20
interval = [-0.001, 1.001]
"""
Itinerary = True
Itinerary_Value = 0.5

def g(x):
    #return 2 * x * (1 - x)
    #return 2.763 * x * (1 - x)
    #return (3*x - x*x*x)/2
    #return 3.3 * x * (1-x)
    #return 3.86 * x * (1-x)
    return 3.84 * x * (1-x)
    #return 4 * x * (1 - x)
    #return 4*x*(1-x)*(1-x*(1-x))
    #return 3 * x % 1

def f(x, iteration = gnx):
    for i in range(0, iteration):
        x = g(x)
    return x
    
 


def main():
    int_x = np.linspace(interval[0], interval[1], 500)
    plt.plot(int_x, f(int_x))
    plt.plot(int_x, int_x)
    plt.grid(True)
    if len(initial_value) == 0:
        plt.show()
        return 
    for kase in range(0, len(initial_value)):
        StringLR = ""
        x = initial_value[kase]
        if Itinerary:
            if x < Itinerary_Value:
                StringLR += "L"
            else:
                StringLR += "R"
        fx = f(initial_value[kase])
        #print("0 " + str(fx))
        plt.plot([x, x], [0, fx], color[kase])
        for i in range(0, iteration_time):
            plt.plot([x, fx], [fx, fx], color[kase])
            #print(str(i + 1) + " " + str(fx))
            x = fx
            if Itinerary:
                if x < Itinerary_Value:
                    StringLR += "L"
                else:
                    StringLR += "R"
            fx = f(x)
            plt.plot([x, x], [x, fx], color[kase])
        if Itinerary:
            print(StringLR)
    plt.show()


if __name__ == '__main__':
    main()
