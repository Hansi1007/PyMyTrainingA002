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