"""
NAME 
   5-SiciliaPablo-LaGrange.py

VERSION
  1.1

AUTHOR
  Pablo Sicilia Andrade  <psicilia@gmail.com>


DESCRIPTION
    programa que aproxima una ecuacion al conjunto de puntos
    por el metodo numerico interpolacion de lagrange

CATEGORY
    metodos numericos
    aproximacion funcional


USAGE
  5-SiciliaPablo-LaGrange.py

GITHUB
    https://github.com/psicilia/proyecto-final/blob/1cd01347085aaec9103a22486dc79181ab3a8702/5-SiciliaPablo-LaGrange.py

"""
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from math import *

x = sp.Symbol('x')
# definimos x como simbolo
print("bienvenido al metodo de lagrange")


listX = []
# lista de x 
listY = []
#lista de y
i = 0
nDatos = int(input("ingresa la cantidad de datos que posees: "))
while i < nDatos:
    # leemos los datos que tengamos
    listX.append(float(eval(input("ingrese el valor de X" + str(i+1) + ": " ))))
    listY.append(float(eval(input("ingrese el valor de y" + str(i+1) + ": " ))))
    i = i + 1


y = 0
i = 0
j = 0
for i in range(len(listX)):
    xi = 1
    ij = 1
    for j in range(len(listX)):
        if i != j:
            xi = xi * (x - listX[j])
            ij = ij * (listX[i] - listX[j])
            #con base en la cantidad de elementos realizamos los productorios

    y = y + ((xi)/(ij))*(listY[i])
    # definimos al ecuacion general con base en los productorios

inter = input("para interpolar ingrese el valor, para ver la ecuacion presione enter: ")
x = np.linspace(listX[0], listX[-1], 100)
if inter == "":
    print(sp.expand(y))
else:
    inter = float(inter)
    result = y.subs(x, inter)
    print(result)
    # si no se ingresa  un valor a interpolar se imprime la ecuacion
funcion = eval(str(y))
plt.plot(listX, listY, marker = 'o', linestyle = ':', color = 'r')
plt.plot(x, funcion, color= 'b')
plt.xlabel('x')
plt.ylabel('y')
plt.title('puntos')
plt.yticks(listY)
plt.xticks(listX)
plt.show()
