"""
NAME 
    3-SiciliaPablo-Falsi.py

VERSION
  1.3

AUTHOR
  Pablo Sicilia Andrade  <psicilia@gmail.com>


DESCRIPTION
    programa que aproxima la raiz de una ecuacion
    por el metodo numerico de Regula falsi

CATEGORY
    metodos numericos
    raices de ecuaciones

USAGE
  3-SiciliaPablo-Falsi.py

GITHUB
    https://github.com/psicilia/proyecto-final/blob/966bcafc1ab154f1d427a45db73828d8c20c36a7/2.0/3-SiciliaPablo-Falsi.py

"""
import matplotlib.pyplot as plt
from math import *
import numpy as np
from sympy import *
import sympy as sp

X, y = sp.symbols("X y")
# definimos x como simbolo
print("bienvenido al metodo de Regula Falsi")

listRes = []
# lista de resultados
i = 0
 
y = eval(input("ingrese su ecuacion: "))
# leemos la ecuacion 
a = float(eval(input("ingrese el valor menor del rango: ")))
b = float(eval(input("ingrese el valor mayor del rango: ")))
#leemos el rango

def error(a,b):
    relativeE = abs((b-a)/b)
    return relativeE
    # definifmos el calculo del error
    
def siguiente(k):
    fk = (y.subs(X, k))
    fx = (y.subs(X,listRes[-1]))
    aprox = (((listRes[-1]*fk)-(k*fx))/(fk-fx))
    return aprox
    # definimos el calculo de la aproximacion siguiente con vase en el pivote k

listRes.append((a*(y.subs(X,b))-(b*(y.subs(X,a))))/((y.subs(X,b))-(y.subs(X,a))))
#agregamos el resultado base  (a f(b) - b f(a)) / f(b)-f(a)

if ((y.subs(X, a) * y.subs(X,listRes[0])) < 0):
    pivot = a
elif ((y.subs(X, b) * y.subs(X,listRes[0])) < 0):
    pivot = b
# seleccionamos el pivote inicial

listRes.append(siguiente(pivot))
print(listRes)
print((y.subs(X,a)))
print((y.subs(X,b)))
i = 1
decimal = int(input("cantidad de decimales: "))
while error(listRes[-1], listRes[-2]) > (10**(-decimal)):
    if (listRes[-1]*listRes[-2] < 0):
        pivot = listRes[-2]
        # cambiamos de pivote si son de difetente signo
    listRes.append(siguiente(pivot))
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