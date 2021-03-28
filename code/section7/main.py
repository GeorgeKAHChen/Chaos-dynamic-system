#==================================================
#
#   Lyapunov exponent calclulator
#
#   main
#
#==================================================

import os
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt

import Init
import Data_Generator

GENERATOR_LOOP = 10
COLOR_LOOP = ["r", "g", "b", "c", "m"]


def main():
    information, initial_val, initial_t, final_t, delta_t, Val_set, Jaco_set = Data_Generator.main(OutputFile = False, initial_val = Val_Set[len(Val_Set)-1], old_information = "", Calc_Jaco = True)
    for ttl in range(0, GENERATOR_LOOP):
        print(ttl, GENERATOR_LOOP)
        
 





if __name__ == '__main__':
    main()

