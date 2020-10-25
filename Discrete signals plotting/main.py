import numpy as np
import matplotlib.pyplot as plt
from bdtsf import unit_impulse, unit_step
from mult_add import multiply, add, multiplySignals


# SIGNAL: x[n] = d[n]u[1-n] + 2u[n+3] - u[n-5] + 3d[n-4]

UL = 10 # upper limit
LL = -10 # lower limit

n =np.arange(LL, UL, 1)

d1 = unit_impulse(0,n)  # d[n]

u1 = unit_step(1, n)
u11 = multiply(-1, u1) # u[1-n]

u2 = unit_step(-3, n)
u22 = multiply(2, u2) # 2u[n+3]

u3 = unit_step(5, n)
u33 = multiply(-1, u3) # -u[n-5]

d2 = unit_impulse(4, n)
d22 = multiply(3, d2) # 3d[n-4]

x1 = multiplySignals(d1, u11)
x2 = add(x1, u22)
x3 = add(x2, u33)

x = add(x3, d22)

plt.stem(n, x)
plt.grid()
plt.xlabel('n') 
plt.xticks(np.arange(LL, UL, 1)) 
plt.yticks([-2, -1, 0, 1, 2, 3, 4, 5]) 
plt.ylabel('x[n]') 
plt.title('Signal x[n]') 

plt.show()
