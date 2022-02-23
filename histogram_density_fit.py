# Michael Hofbauer ~ hofbauer@uab.edu
# Let X ~ N(0,1) and Y = exp(X).
# We are plotting the pdf
# f_Y(y) = 1/sqrt(2\pi) exp(-1/2(ln y)^2)1/y
# together with a histogram of randomly generated
# (y_1,...,y_n), where y_i = exp(x_i) and
# (x_1,...,x_n) are randomly generated standard normals.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Probability density function of Y
def f(y):
    return 1/np.sqrt(2*np.pi) * 1/np.reciprocal(y) * np.exp(-0.5*np.log(y)*np.log(y))

# n ... length of interval [0,n]
# r ... number of ticks in the interval [0,n]

def plot(n,r):
    n_prob = np.linspace(0.01, n, num = r)
    norm_x = norm.rvs(size = 10000)
    r_y = np.exp(norm_x)
    plt.figure(figsize = (20,18))
    plt.title('Histogram comparision to pdf of Y = exp(X), X ~ N(0,1)', fontsize = 22)
    plt.hist(r_y, 50, facecolor='g', density = True, label = 'Histogram')
    plt.plot(n_prob, f(n_prob), 'b', label = 'PDF of Y = exp(X)')
    plt.xlabel('Y data points', fontsize = 22)
    plt.ylabel('f(Y)', fontsize = 22)
    plt.xlim(0,30)
    plt.grid(True)
    plt.legend(loc = 'center right', fontsize = 'xx-large')
    plt.show()
