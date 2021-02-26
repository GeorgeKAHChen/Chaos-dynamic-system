import random
import numpy as np
import matplotlib.pyplot as plt
import time

iteration_time = 1200
mark_iter = 1000
x_axis = 7
initial_set = []
for kase in range(0, 1000):
    time.sleep(0.01)
    initial_set.append(random.random())
val_set = []

for kase in range(0, len(initial_set)):
    val_x = initial_set[kase]
    for i in range(0, iteration_time):
        prob = random.random()
        if prob > 0.5:
            val_x = val_x / 3
        else:
            val_x = (2 + val_x) / 3
        if i > mark_iter:
            val_set.append(val_x)

stats_x = np.arange(0, 1, pow(1/3, x_axis))

plt.hist(val_set, stats_x, density=True)

plt.show()