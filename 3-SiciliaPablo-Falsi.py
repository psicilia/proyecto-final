import sympy as sp
from math import *

from sympy.polys.partfrac import apart

x = sp.Symbol('x')
print("bienvenido al metodo de Regula Falsi")

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

