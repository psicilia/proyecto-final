"""
NAME 
    1-SiciliaPablo-Aprox.py

VERSION
  1.1

AUTHOR
  Pablo Sicilia Andrade  <psicilia@gmail.com>


DESCRIPTION
    programa que aproxima la raiz de una ecuacion
    por el metodo numerico de Aproximaciones sucesivas

CATEGORY
    metodos numericos
    raices de ecuaciones

USAGE
  1-SiciliaPablo-Aprox.py

GITHUB
    https://github.com/psicilia/proyecto-final/blob/1cd01347085aaec9103a22486dc79181ab3a8702/1-SiciliaPablo-Aprox.py

"""

import matplotlib.pyplot as plt
import numpy as np
from math import *
from sympy import *
import sympy as sp

x = sp.Symbol('x')
# definimos x como simbolo
print("bienvenido al metodo de aproximaciones sucesivas")

listX = [] #lista de valores de X 
listY = []
y = eval(input("ingrese la ecuacion original"))
ecuacion = eval(input("ingrese el despeje de su ecuacion: "))
# leemos la ecuacion de teclado
listX.append(float(eval(input("ingresa un valor: "))))
# agregamos el valor inicial de x a la lista
decimal = int(input("cantidad de decimales: "))
# leemos la cantidad de decimales a utilizar

listY.append(round(y.subs(x, listX[-1]), decimal))
def error(x,y):
    if y == 0:
        relativeE = abs(y-x)
    else:
        relativeE = abs((y-x)/y)

    return relativeE
    #definimos el calculo del error relativo

i = 1
listX.append(ecuacion.subs(x, listX[-1]))
listY.append(round(y.subs(x, listX[-1]), decimal))
print(listX[-1])
#obtenemos el valor de x1 

while (error(listX[-1], listX[-2]) > (10**(-decimal))):
    # si el error entre xi+1 y xi es mayor que el margen continuamos 
    listX.append(ecuacion.subs(x, listX[-1]))
    listY.append(round(y.subs(x, listX[-1]), decimal))
    print(listX[-1])
    i = i + 1

print("converge a" + str(decimal) + " decimales en " + str(round(listX[-1], decimal)) + " con " + str(i) + " iteraciones")
# mostramos el ultimo elemento calculado de la lista de x

#print("no converge con el valor de x aproximado")


print(ecuacion)

x = np.linspace(float(listX[-1]-1), float(listX[-1]+1), 100)
a = [float(listX[-1]-1),float(listX[-1]+1)]
b = [0,0]
funcion = eval(str(y))
print('y', type(funcion))
plt.plot(listX, listY, marker='o', linestyle=':')
plt.plot(x, funcion, color= 'b')
plt.plot(a,b)
plt.xlabel('x')
plt.ylabel('y')
plt.title(y)
plt.show()