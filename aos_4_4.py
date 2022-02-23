# We check for X_1,...,X_n ~ Bernoulli(p),
# how well the confidence interval
# (\hat{p}-\eps_n, \hat{p}+\eps_n) obtained from
#  Hoeffding's inequality covers the true
#  parameter p.

import numpy as np
import matplotlib.pyplot as plt

def CI(alpha,p,n,r):
    
