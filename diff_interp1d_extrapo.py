import numpy as np
import matplotlib.pyplot as plt

def vektorfeld2(x, y):
    dx = 1 #dx/dy ist nicht abhängig von
    dy = 2 * x * y
    return dx , dy

def vektorfeld(x, y):
    dx = 1 #dx ist konstant
    dy = 2 * np.sqrt(y -1) # dy/dy = 2 * wurzel von y-1
    return dx , dy


# Erzeuge ein Gitter mit Punkten    
x = np.linspace(0, 10, 20)   
y = np.linspace(1.1, 10, 20)
X , Y = np.meshgrid(x, y)

# Berechne die Komponnenten des Vektrofeldes
U, V = vektorfeld(X, Y)
plt.quiver(X, Y, U, V)
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Vektorfeld $\frac{dy}{dx} = 2 \sqrt{y-1}$')
plt.grid()
plt.show()

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def differential_equation(x, y):
    return 2* np.sqrt(y-1)
#Anfangsbedingungen    
x0 = 0
y0 = 2 # setze einen Anfangswert für y ( muss grösser als 1 sein z.b y0 = 2)

# Lösungsbereich 
x_span = [x0, 10]

solution = solve_ivp(differential_equation, x_span, [y0], dense_output=True)

# Berechne die Lösungspunkte
x_values = np.linspace(x0, 10, 100)
y_values = solution.sol(x_values)[0]

plt.plot(x_values, y_values, label=r'$\frac{dy}{dx} = 2 \sqrt{y-1}$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()

def vektorfeld3(x, y):
    dx = 1 # dx ist konstant
    dy = y -2 * x # dy/dx = y - 2x
    return dx , dy
    
# Erzeuge ein Gitter mit Punkten    
x = np.linspace(-1, 1, 20)   
y = np.linspace(-1, 1, 20)
X , Y = np.meshgrid(x, y)

# Berechne die Komponnenten des Vektrofeldes
U, V = vektorfeld3(X, Y)

plt.quiver(X, Y, U, V)
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Vektorfeld $\frac{dy}{dx} = y - 2x$')
plt.grid()
plt.show()

def differential_equation3(x, y):
    return  y - (2 * x)
#Anfangsbedingungen    
x0 = 1
y0 = 0 # setze einen Anfangswert für y 

# Lösungsbereich 
x_span = [x0, 10]

solution = solve_ivp(differential_equation3, x_span, [y0], dense_output=True)

# Berechne die Lösungspunkte
x_values = np.linspace(x0, 10, 100)
y_values = solution.sol(x_values)[0]

plt.plot(x_values, y_values, label=r'$\frac{dy}{dx} = y - 2x$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
x = np.array([
24.000,
54.000,
68.500,
69.350,
73.000
])

y = np.array([
    -0.280,           #24.0
    -0.160,           #54.0    
    -0.100,           #68.5
    -0.0,             #69.35
    -0.0,             #73.0
    ])
    
x_new = np.array([
0.000,
2.000,
4.000,
6.000,
8.000,
10.000,
13.000,
19.000,
48.000,
52.000,
56.900,
58.900,
61.000,
62.400,
64.200,
65.400,
66.600,
68.000,
69.500,
69.600,
69.700,
69.800,
69.900,
70.000,
70.100,
70.350,
])



# f = interp1d(x, y, kind = 'linear')
f = interp1d(x, y, kind = 'linear', fill_value='extrapolate')
y_new = f(x_new)

for xn,yn in zip(x_new, y_new):
    print(xn,yn)
    
plt.plot(y,x,'o', label = 'Urdaten')
plt.plot(y_new, x_new, '-', label='Interpolierte Daten')
plt.legend()
plt.grid()
plt.show()