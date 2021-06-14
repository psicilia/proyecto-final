from mpmath.functions.functions import re
import sympy as sp
from math import *

from sympy.polys.partfrac import apart

x = sp.Symbol('x')
print("bienvenido al metodo de lagrange")

#listX = [-5.0,-3.0,0.0,3.0,5.0]
listX = []
#listY = [2.0,-1.0,4.0,6.0,1.0]
listY = []
i = 0
nDatos = int(input("ingresa la cantidad de datos que posees: "))
while i < nDatos:
    listX.append(float(input("ingrese el valor de X" + str(i+1) + ": " )))
    listY.append(float(input("ingrese el valor de y" + str(i+1) + ": " )))
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

    y = y + ((xi)/(ij))*(listY[i])

inter = input("para interpolar ingrese el valor, para ver la ecuacion presione enter: ")
if inter == "":
    print(sp.expand(y))
else:
    inter = float(inter)
    result = y.subs(x, inter)
    print(result)

"""
listRes = []
i = 0

ecuacion = input("ingrese su ecuacion: ")
y = eval(ecuacion)
a = float(input("ingrese el valor menor del rango: "))
b = float(input("ingrese el valor mayor del rango: "))

def error(a,b):
    relativeE = abs((b-a)/b)
    return relativeE
    
def siguiente(k):
    fk = (y.subs(x, k))
    fx = (y.subs(x,listRes[-1]))
    aprox = (((listRes[-1]*fk)-(k*fx))/(fk-fx))
    return aprox

listRes.append((a*(y.subs(x,b))-(b*(y.subs(x,a))))/((y.subs(x,b))-(y.subs(x,a))))

if (y.subs(x, a) * y.subs(x,listRes[0])) < 0:
    pivot = a
elif (y.subs(x, b) * y.subs(x,listRes[0])) < 0:
    pivot = b

listRes.append(siguiente(pivot))
print(listRes)
print((y.subs(x,a)))
print((y.subs(x,b)))
i = 1
decimal = int(input("cantidad de decimales: "))
while error(listRes[-1], listRes[-2]) > (10**(-decimal)):
    if (listRes[-1]*listRes[-2] < 0):
        pivot = listRes[-2]
    listRes.append(siguiente(pivot))
    i = i + 1
print(listRes)
print(" converge a "+ str(decimal) +" decimales en "+ str(round(listRes[-1],decimal)) +" con "+ str(i) + " iteraciones" )
"""
