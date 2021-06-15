from mpmath.libmp.libintmath import list_primes
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

def k1():
    res = h*(f.subs(x, listX[-1]).subs(y, listY[-1]))
    return res
def k2():
    res = h*(f.subs(x, (listX[-1] + (h/2))).subs(y, (listY[-1] + (k1()/2))))
    return res
def k3():
    res = h*(f.subs(x, (listX[-1] + (h/2))).subs(y, (listY[-1] + (k2()/2))))
    return res
def k4():
    res = h*(f.subs(x, (listX[-1] + h)).subs(y, (listY[-1]) + k3()))
    return res

while i <= s:
    newY = listY[-1] + (1/6)*(k1() + 2*k2() + 2*k3()+ k4())
    listY.append(newY)
    listX.append(i)
    i = round(i + h, 5)
print
print(listY[-1])

