# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

x = sp.Symbol('x')

# Creating vectors X and Y
listX = [1,2,3,4,6,8,9,10]
listY = [2,4,3,3,5,5,4,6]

x = np.linspace(listX[0], listX[-1], 100)
funcion = eval("0.000264550264550265*x**7 - 0.010515873015873*x**6 + 0.17744708994709*x**5 - 1.6359126984127*x**4 + 8.72228835978834*x**3 - 25.9964285714285*x**2 + 38.5999999999999*x - 17.8571428571429")

# Create the plot

print(type(x))
print(type(funcion))
plt.plot(listX, listY, marker='o', linestyle=':')
plt.plot(x, funcion)
plt.yticks(listY)


# Show the plot
plt.show()