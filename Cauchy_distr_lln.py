# Michael Hofbauer ~ hofbauer@uab.edu

# Let X_1,..., X_n ~ N(0,1) and Y_1,...,Y_n ~ Cauchy.
# We plot f_X(n) = \bar{X_n} f_Y(n) = \bar{Y_n},
# where f_X(n), f_Y(n) are the sample means,
# to illustrate that f_X(n) converges to 0,
# but due to the thick tails of the Cauchy distribution,
# f_Y(n) diverges (i.e. Cauchy distribution has infinite moments 
# and therefore does not satisfy the preassumptions for the LLN).

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import cauchy, norm

normal_sample_mean_list = []
cauchy_sample_mean_list = []

def plot_sm(n,r):
    ticks_raw = np.linspace(1, n, num = r)
    ticks_n = [int(np.ceil(x)) for x in ticks_raw]
    for j in ticks_n:
        std_normals = norm.rvs(size = j)
        cauchy_sample = cauchy.rvs(size = j)
        normal_sample_mean_list.append((1/j)*np.sum(std_normals))
        cauchy_sample_mean_list.append((1/j)*np.sum(cauchy_sample))
    # Begin with plot
    plt.figure(figsize = (18,15))
    plt.title('Comparision of normal N(0,1) and Cauchy distributed sample mean sequences', fontsize = 22)
    plt.plot(ticks_n, normal_sample_mean_list, marker = 'p', color = 'b', label = 'Normal sample mean')
    plt.plot(ticks_n, cauchy_sample_mean_list, '^r', label = 'Cauchy sample mean')
    plt.xlabel('Sample size', fontsize = 22)
    plt.ylabel('Sample mean values', fontsize = 22)
    # plt.xlim(0,30)
    plt.grid(True)
    plt.legend(loc = 'best', fontsize = 'xx-large')
    plt.show()
