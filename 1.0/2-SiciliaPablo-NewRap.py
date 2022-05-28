"""
NAME 
    2-SiciliaPablo-NewRap.py

VERSION
  1.1

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
    https://github.com/psicilia/proyecto-final/blob/1cd01347085aaec9103a22486dc79181ab3a8702/2-SiciliaPablo-NewRap.py

"""

import sympy as sp
from math import *

x = sp.Symbol('x')
# definimos x como simbolo
print("bienvenido al metodo de Newton Rapson")

# lista de coeficientes 
listEsc = []
# lista de resultados
listRes = []

i = 0
#inicializamos ecuacion 
ecuacion = ""
ecuacion = input("ingrese su ecuacion: ")
y = eval(ecuacion)

# mostramos la ecuacion final
print(ecuacion)
y = eval(ecuacion)

def error(a,b):
    #definimos el calculo del error relativo
    relativeE = abs((b-a)/b)
    return relativeE
    
# derivamos y con respecto a x
derivada = y.diff(x)

def siguiente():
    # definimos el calculo del siguiente resultado
    aprox = (x-(y/derivada))
    return aprox.subs(x, (listRes[-1]))

decimal = int(input("cantidad de decimales: "))
#leemos la precision y el valor inicial
listRes.append(float(eval(input("ingrese valor inicial: "))))
# calculamos el resultado calculando con el valor inicial
listRes.append(siguiente())
i = 1
while error(listRes[-1], listRes[-2]) > (10**(-decimal)):
    # si el error de los resultados es mayor al margen seguimos calculando 
    listRes.append(siguiente())
    i = i + 1
print(" converge a "+ str(decimal) +" decimales en "+ str(round(listRes[-1],decimal)) +" con "+ str(i) + " iteraciones" )