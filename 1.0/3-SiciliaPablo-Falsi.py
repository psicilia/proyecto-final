"""
NAME 
    3-SiciliaPablo-Falsi.py

VERSION
  1.1

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
    https://github.com/psicilia/proyecto-final/blob/1cd01347085aaec9103a22486dc79181ab3a8702/3-SiciliaPablo-Falsi.py

"""
import sympy as sp
from math import *

x = sp.Symbol('x')
# definimos x como simbolo
print("bienvenido al metodo de Regula Falsi")

listRes = []
# lista de resultados
i = 0

ecuacion = input("ingrese su ecuacion: ")
y = eval(ecuacion)
# leemos la ecuacion 
a = float(eval(input("ingrese el valor menor del rango: ")))
b = float(eval(input("ingrese el valor mayor del rango: ")))
#leemos el rango

def error(a,b):
    relativeE = abs((b-a)/b)
    return relativeE
    # definifmos el calculo del error
    
def siguiente(k):
    fk = (y.subs(x, k))
    fx = (y.subs(x,listRes[-1]))
    aprox = (((listRes[-1]*fk)-(k*fx))/(fk-fx))
    return aprox
    # definimos el calculo de la aproximacion siguiente con vase en el pivote k

listRes.append((a*(y.subs(x,b))-(b*(y.subs(x,a))))/((y.subs(x,b))-(y.subs(x,a))))
#agregamos el resultado base  (a f(b) - b f(a)) / f(b)-f(a)

if (y.subs(x, a) * y.subs(x,listRes[0])) < 0:
    pivot = a
elif (y.subs(x, b) * y.subs(x,listRes[0])) < 0:
    pivot = b
# seleccionamos el pivote inicial

listRes.append(siguiente(pivot))
print(listRes)
print((y.subs(x,a)))
print((y.subs(x,b)))
i = 1
decimal = int(input("cantidad de decimales: "))
while error(listRes[-1], listRes[-2]) > (10**(-decimal)):
    if (listRes[-1]*listRes[-2] < 0):
        pivot = listRes[-2]
        # cambiamos de pivote si son de difetente signo
    listRes.append(siguiente(pivot))
    i = i + 1
print(" converge a "+ str(decimal) +" decimales en "+ str(round(listRes[-1],decimal)) +" con "+ str(i) + " iteraciones" )

