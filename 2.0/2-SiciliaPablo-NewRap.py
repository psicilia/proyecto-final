"""
NAME 
    2-SiciliaPablo-NewRap.py

VERSION
  1.2

AUTHOR
  Pablo Sicilia Andrade  <psicilia@gmail.com>


DESCRIPTION
    programa que aproxima la raiz de una ecuacion
    por el metodo numerico de Newton-Raphson

CATEGORY
    metodos numericos
    raices de ecuaciones

USAGE
  2-SiciliaPablo-NewRap.py

GITHUB
    https://github.com/psicilia/proyecto-final/blob/966bcafc1ab154f1d427a45db73828d8c20c36a7/2.0/2-SiciliaPablo-NewRap.py

"""
import matplotlib.pyplot as plt
from math import *
import numpy as np
from sympy import *
import sympy as sp

X, y = sp.symbols("X y")
# definimos X como simbolo
print("bienvenido al metodo de Newton Rapson")

# lista de resultados
listRes = []

#inicializamos ecuacion 

y = eval(input("ingrese su ecuacion: "))
# mostramos la ecuacion final

def error(a,b):
    #definimos el calculo del error relativo
    relativeE = abs((b-a)/b)
    return relativeE
    
# derivamos y con respecto a x
derivada = y.diff(X)

def siguiente():
    # definimos el calculo del siguiente resultado
    aprox = (X-(y/derivada))
    return aprox.subs(X, (listRes[-1]))

listRes.append(float(eval(input("ingrese valor inicial: "))))
# calculamos el resultado calculando con el valor inicial
decimal = int(input("cantidad de decimales: "))
#leemos la precision y el valor inicial
listRes.append(siguiente())
i = 1
while error(listRes[-1], listRes[-2]) > (10**(-decimal)):
    # si el error de los resultados es mayor al margen seguimos calculando 
    listRes.append(siguiente())
    i = i + 1
print(" converge a "+ str(decimal) +" decimales en "+ str(round(listRes[-1],decimal)) +" con "+ str(i) + " iteraciones" )

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