# Basic Discrete Time Signal Functions

# import libraries
import numpy as np
import matplotlib.pyplot as plt

# a - Enter delay or advance

# Impulse d(a)
def unit_impulse(a, n):
    delta = []
    for sample in n:
        if (sample == a):
            delta.append(1)
        else:
            delta.append(0)
    return delta


# Unit Step u[n-a]
def unit_step(a, n):
    unit = []
    for sample in n:
        if (sample < a):
            unit.append(0)
        else:
            unit.append(1)

    return (unit)


# Unit ramp r[n]
# r[n] = n for n >= 0, r[n] = 0 otherwise
def unit_ramp(n):
    ramp = []
    for sample in n:
        if (sample < 0):
            ramp.append(0)
        else:
            ramp.append(sample)
    return ramp


# Exponential signals e**(at)
def exponential(a, n):
    expo = []
    for sample in n:
        expo.append(np.exp(a * sample))
    return (expo)



