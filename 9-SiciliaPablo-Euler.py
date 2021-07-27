"""
NAME 
   9-SiciliaPablo-Euler.py
VERSION
  1.1

AUTHOR
  Pablo Sicilia Andrade  <psicilia@gmail.com>


DESCRIPTION
    programa que extrapola el resultado de una ecuacion diferencial
    por el metodo numerico de Euler

CATEGORY
    metodos numericos
    Ecuaciones diferenciales

USAGE
  9-SiciliaPablo-Euler.py
GITHUB


"""
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
#lista de valores de y

h = float(input("ingrese el valor del paso: "))
listY.append(float(eval(input("ingrese el valor de y correspondiente a x = 0: "))))
listX.append(0.0)
s = float(eval(input("ingrese el valor de x que desea: ")))
# leemos los datos especiales y definimos los primeros valores de x, y
i = h

while i <= s:
    newY = listY[-1] + h*(f.subs(x, listX[-1]).subs(y, listY[-1]))
    listY.append(newY)
    listX.append(i)
    i = i + h
# repetimos el calculo para llegar de xo a la x que queremos definir
print(listY[-1])




