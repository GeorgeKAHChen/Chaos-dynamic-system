import numpy as np
import matplotlib.pyplot as plt

initial_value = [-2, -1.7, -0.3, 0, 0.1, 1.9]
color = ["r-", "g-", "b-", "c-", "m-", "y-"]
iteration_time = 10
interval = [-2.2, 2.2]

def f(x):
    #return 2 * x * (1 - x)
    return (3*x - x*x*x)/2


def main():
    int_x = np.linspace(interval[0], interval[1], 500)
    plt.plot(int_x, f(int_x))
    plt.plot(int_x, int_x)
    for kase in range(0, len(initial_value)):
        x = initial_value[kase]
        fx = f(initial_value[kase])
        print("0 " + str(fx))
        plt.plot([x, x], [0, fx], color[kase])
        for i in range(0, iteration_time):
            plt.plot([x, fx], [fx, fx], color[kase])
            x = fx
            fx = f(x)
            plt.plot([x, x], [x, fx], color[kase])
            print(str(i+1) + " " + str(fx))
    
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
