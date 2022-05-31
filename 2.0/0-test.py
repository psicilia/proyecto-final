# Import libraries
import matplotlib.pyplot as plt
from math import *
import numpy as np
from sympy import *
import sympy as sp

X, y = sp.symbols("X y")

# Creating vectors X and Y
listX = [1,10]
listY = []
print(type(listX))
print(type(listY))

funcion = 5*sin(X)
x = np.linspace(listX[0], listX[-1], 100)
for a in x:
	listY.append(funcion.subs(X, a))

# Create the plot

print(type(x))
print(type(funcion))
plt.plot(x, listY)
# Show the plot
plt.show()