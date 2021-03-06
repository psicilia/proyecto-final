"""
NAME 
   9-SiciliaPablo-Euler.py
VERSION
  1.2

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
    https://github.com/psicilia/proyecto-final/blob/966bcafc1ab154f1d427a45db73828d8c20c36a7/2.0/9-SiciliaPablo-Euler.py

"""
import matplotlib.pyplot as plt
from math import *
import numpy as np
from sympy import *
import sympy as sp

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

evaluado = []
evaluadoP = []
x = np.linspace(float(min(listRes)-1), float(max(listRes)+1), 100)
for a in x:
    evaluado.append(y.subs(X, a))
for a in listRes:
    evaluadoP.append(y.subs(X, a))

a = [float(min(listRes)-1), float(max(listRes)+1)]
b = [0, 0]
c = [float(min(evaluadoP)-1), float(max(evaluadoP)+1)]

plt.plot(listRes, evaluadoP, marker='o', linestyle=':', color = 'r')
plt.plot(x, evaluado, color= 'b')
plt.plot(a,b, color = 'black')
plt.plot(b,c, color = 'black')
plt.xlabel('x')
plt.ylabel('y')
plt.title(y)
plt.show()

