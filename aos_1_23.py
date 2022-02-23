# Visualization of conditional probability.

import random
import numpy as np
import matplotlib.pyplot as plt
import math
from prettytable import PrettyTable as pt
from scipy import stats

# table = pt()
# table.field_names = ['P(A)P(B)', 'P(AB)']
# print(table)

# A, B independent events.
A = (2,4,6)
B = (1,2,3,4)
AB = (2,4)

def cond(n,r):
    probability_A_B = []
    probability_AB = []
    print('{0:20s} {1:10s}'.format('P(A)P(B)','P(AB)'))
    # data_list = []
    n_raw = np.linspace(0, n, num = r)
    ticks_list = [math.ceil(x) for x in n_raw]
    ticks_list.remove(0)
    for j in ticks_list:
        total_die_rolls = random.choices((1,2,3,4,5,6), k = j)
        A_elements = [x for x in total_die_rolls if x in A]
        B_elements = [y for y in total_die_rolls if y in B]
        AB_elements = [z for z in total_die_rolls if z in AB]
        PRAPRB, PRAB = (len(A_elements)/j)*(len(B_elements)/j), len(AB_elements)/j
        print('{0:10f}{1:10f}'.format(PRAPRB,PRAB))
        probability_A_B.append(PRAPRB)
        probability_AB.append(PRAB)
        # len(A_elements)/j, len(B_elements)/j,
        # PR = len(A_elements)/j*len(B_elements)/j, len(AB_elements)/j
        # data_list.extend(PR)
        # print(data_list)
        # table.add_row(data_list)
        # data_list = []
    print(f'\n The number of simulations is {len(ticks_list)}.\n')
    print(f' The total number of die rolls in each simulation is given in the list: {ticks_list}')
    reg = stats.linregress(probability_A_B,probability_AB)
    plt.figure(figsize = (20,18))
    # plt.xticks(probability_A_B, fontsize = 16)
    # plt.yticks(probability_AB, fontsize = 16)
    plt.title('''Verifying the relation P(A)P(B) = P(AB) for independent events A, B numerically.
    ''', fontsize = 22)
    plt.plot(probability_A_B, probability_AB, 'o', label = 'P(A)P(B) = P(AB)')
    plt.plot([0,1],[reg.intercept, reg.intercept + reg.slope], 'r', label='fitted line')
    # plt.plot(probability_A_B, reg.intercept + reg.slope*probability_A_B, 'g')
    plt.xlabel('P(A)P(B)')
    plt.ylabel('P(AB)')
    plt.legend()
    plt.show()
        # print(table)
