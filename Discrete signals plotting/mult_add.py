import numpy as np
import matplotlib.pyplot as plt


# Multiply
# amp - number for multipy
# l - list for signal
def multiply(amp, l):
    n_list = []
    for i in l:
        n_list.append(i * amp)
    return n_list


# Add
def add(l1, l2):
    l_r = []
    for i in range(0, len(l1)):
        l_r.append(l1[i] + l2[i])
    return l_r


# Multipy signals(lists)
def multiplySignals(s1, s2):
    c = np.multiply(s1, s2)
    return c
