from sympy import *
from math import *
import numpy as np

x, y = symbols('x y')
ecuacion = input("ingrese su ecuacion: ")
f = eval(ecuacion)
listX = []
listY = []

h = float(input("ingrese el valor del paso: "))
listY.append(float(input("ingrese el valor de y correspondiente a x = 0: ")))
listX.append(0.0)
s = float(input("ingrese el valor de x que desea: "))
i = h


while i <= s:
    newY = listY[-1] + h*(f.subs(x, listX[-1]).subs(y, listY[-1]))
    listY.append(newY)
    listX.append(i)
    i = i + h
print(listY[-1])




