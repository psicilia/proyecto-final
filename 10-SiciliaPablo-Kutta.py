"""
NAME 
   10-SiciliaPablo-Kutta.py
VERSION
  1.1

AUTHOR
  Pablo Sicilia Andrade  <psicilia@gmail.com>


DESCRIPTION
    programa que extrapola el resultado de una ecuacion diferencial
    por el metodo numerico de Runge-Kutta

CATEGORY
    metodos numericos
    Ecuaciones diferenciales

USAGE
  10-SiciliaPablo-Kutta.py

GITHUB
    https://github.com/psicilia/proyecto-final/blob/1cd01347085aaec9103a22486dc79181ab3a8702/10-SiciliaPablo-Kutta.py

"""
from mpmath.libmp.libintmath import list_primes
import sympy as sp
from math import *
import numpy as np

x, y = sp.symbols('x y')
# definimos x, y como simbolos
ecuacion = input("ingrese su ecuacion: ")
f = eval(ecuacion)
#leemos la ecuacion 
listX = []
# lista de valores de x 
listY = []
# lista de valores de y

h = float(input("ingrese el valor del paso: "))
listY.append(float(eval(input("ingrese el valor de y correspondiente a x = 0: "))))
listX.append(0.0)
s = float(eval(input("ingrese el valor de x que desea: ")))
# leemos los datos especiales y definimos los primeros valores de x, y
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
    # calculamos con base en las definiciones de k1, k2, k3, k4 y ek ultimo elemento de x, y
    listY.append(newY)
    listX.append(i)
    i = round(i + h, 5)
print
print(listY[-1])

