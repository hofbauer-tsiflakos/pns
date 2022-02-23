# Illustration of the law of large numbers
# with Bernoulli distributed coin flips.
import random
import numpy as np
import matplotlib.pyplot as plt
import math

total_heads_proportion = []

def plot_freq(n, r, p):
    n_raw = np.linspace(0, n, num = r)
    ticks_list = [math.ceil(x) for x in n_raw]
    ticks_list.remove(0)
    # if n not in ticks:
    #     ticks.append(n)
    # List of heads (H) and tails (T) with appropriate biased probability p = 0.3.
    for j in ticks_list:
        heads_tails_list = random.choices('HT', [p, 1-p], k = j)
        heads_only = [i for i in heads_tails_list if i == 'H']
        heads_proportion = len(heads_only)/j
        total_heads_proportion.append(heads_proportion)
    print(f'\n The list of ticks is: {ticks_list}',end ='\n\n' )
    print(f' Total heads proportions for {r} trials: {total_heads_proportion}')
    plt.figure(figsize = (12,8))
    plt.xticks(ticks_list, fontsize = 16)
    plt.yticks(total_heads_proportion, fontsize = 16)
    plt.plot(ticks_list, total_heads_proportion, 'ob')
    # plt.legend()
    plt.xlabel(f'''Display of function f(n) = # of heads / n, where
    the trial number is given by the list of ticks (see above) on the x-axis and p = {p}.''')
    plt.show()
