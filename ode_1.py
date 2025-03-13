"""

### pycse - solving first order differential equations in Python
https://www.youtube.com/watch?v=4H0Qr-gxMN4

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# f'(x) = 3 * x**2 + 12 * x -4
def fprime(x, y):
    return 3 * x**2 + 12 * x -4
    
tspan = (-8,4)
F0 = (120, )

sol = solve_ivp(fprime, tspan, F0)
print(sol)

"""
Beispiel: Analytische Lösung
Wir betrachten im Folgenden die DGL:

dy(t)dt=f(t,y(t))=y(t)−t2+1,mit:0≤t≤2,y(0)=α=0.5.
 
Zunächst definieren wir uns die DGL als sympy-Gleichung
"""

# https://itp.uni-frankfurt.de/~hanauske/VPROG/Python/Jupyter/DGL_1.html
from sympy import *

# f'(x) = 3 * x**2 + 12 * x -4
t= symbols('t',real=True)
y = Function('y')(t)
DGL = Eq(y.diff(t), y-t**2 +1)
DGL