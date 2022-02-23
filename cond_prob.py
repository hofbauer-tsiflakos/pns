# Michael Hofbauer ~ hofbauer@uab.edu
# Visualization and regression of conditional probability and indpendent events.

import random
import numpy as np
import matplotlib.pyplot as plt
import math
# from prettytable import PrettyTable as pt
from scipy import stats

# A, B independent events of a die roll.
A = (2,4,6)
B = (1,2,3,4)
AB = (2,4)

# We want to check the valid independence clause P(A \cap B) = P(A)P(B) 
# through a linear regression of simulated die roll samples. 
# The simulated probabilities are the relative frequencies.

# n ... length of interval [0,n].
# r ... number of ticks in the interval [0,n].
def cond(n,r):
    probability_A_B = []
    probability_AB = []
    print('{0:20s} {1:10s}'.format('P(A)P(B)','P(AB)'))
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
    print(f'\n The number of simulations is {len(ticks_list)}.\n')
    print(f' The total number of die rolls in each simulation is given in the list: {ticks_list}')
    reg = stats.linregress(probability_A_B,probability_AB)
    plt.figure(figsize = (20,18))
    plt.title('''Verifying the relation P(A)P(B) = P(AB) for independent events A, B numerically.
    ''', fontsize = 22)
    plt.plot(probability_A_B, probability_AB, 'o', label = 'P(A)P(B) = P(AB)')
    plt.plot([0,1],[reg.intercept, reg.intercept + reg.slope], 'r', label='fitted line')
    plt.xlabel('P(A)P(B)')
    plt.ylabel('P(AB)')
    plt.legend()
    plt.show()
        
