import numpy as  np
import scipy as sp
import sympy as smp
from scipy.misc import derivative

x, a, b, c = smp.symbols('x a b c', real=True)
f = smp.exp(-a*smp.sin(x**2)) * smp.sin(b**x) * smp.log(c*smp.sin(x)**2 / x)
print(smp.latex(f))
print(f)
dfdx = smp.diff(f,x)
print(dfdx)
print("-----------------------------")
print(smp.latex(dfdx))

"""
$$c = \sqrt{a^2 + b^2}$$

$$e^{- a \sin{\left(x^{2} \right)}} \log{\left(\frac{c \sin^{2}{\left(x \right)}}{x} \right)} \sin{\left(b^{x} \right)}$$

***Test***

$$- 2 a x e^{- a \sin{\left(x^{2} \right)}} \log{\left(\frac{c \sin^{2}{\left(x \right)}}{x} \right)} \sin{\left(b^{x} \right)} \cos{\left(x^{2} \right)} + b^{x} e^{- a \sin{\left(x^{2} \right)}} \log{\left(b \right)} \log{\left(\frac{c \sin^{2}{\left(x \right)}}{x} \right)} \cos{\left(b^{x} \right)} + \frac{x \left(\frac{2 c \sin{\left(x \right)} \cos{\left(x \right)}}{x} - \frac{c \sin^{2}{\left(x \right)}}{x^{2}}\right) e^{- a \sin{\left(x^{2} \right)}} \sin{\left(b^{x} \right)}}{c \sin^{2}{\left(x \right)}}$$
"""

f2 = 3*x**2
dfdx = smp.diff(f2, x)
dfdx

# Generate LaTeX output
latex_f2 = smp.latex(f2)
latex_dfdx = smp.latex(dfdx)

print(latex_f2)
print(latex_dfdx)

latex_f = smp.latex(f)
print(latex_f)

"""

"""

"""
ausgabe in latex erzeugen


"""

"""
To generate LaTeX output for the expression `f` and its derivative `dfdx`, you can use the `smp.latex()` function from the `sympy` library. Here's the code to do that:


"""

"""

This code will output the LaTeX representations of the function `f` and its derivative `dfdx`.

"""