"""
NAME 
   8-SiciliaPablo-Romberg.py
VERSION
  1.1

AUTHOR
  Pablo Sicilia Andrade  <psicilia@gmail.com>


DESCRIPTION
    programa que realiza una integracion numerica
    por el metodo numerico de Romberg

CATEGORY
    metodos numericos
    integracion numerica

USAGE
  8-SiciliaPablo-Romberg.py

GITHUB
    https://github.com/psicilia/proyecto-final/blob/1cd01347085aaec9103a22486dc79181ab3a8702/8-SiciliaPablo-Romberg.py

"""
import matplotlib.pyplot as plt
from math import *
import numpy as np
from sympy import *
import sympy as sp

x = sp.Symbol('x')
print("bienvenido al metodo de Romberg")

listRes = []
listJ = []

ecuacion = input("ingrese su ecuacion: ")
expr = eval(ecuacion)
#leemos la ecuacion
a = float(eval(input("ingrese el valor menor del intervalo: ")))
b = float(eval(input("ingrese el valor mayor del intervalo: ")))
c = (b-a)
#definimos el intervalo 

def error(a,b):
    relativeE = abs(b-a)
    return relativeE
    #definimos la operacion para calcular el error relativo

listJ.append((expr.subs(x,a) + expr.subs(x,b))/2)
# definimos J1 

listRes.insert(0, [float(c*listJ[0])])
#calculamos I1 

divisors = []
def siguiente(i):
    iterationResults = []
    divisors.append(int(2**(i-1)))
    #calculamos el valor de el divisor con base en la canridad de iteraciones 
    nextJ = listJ[-1]

    for dividendo in range(divisors[-1])[1:divisors[-1]:2]:
        nextJ = nextJ + expr.subs(x, (a + ((dividendo/divisors[-1]) * c)))
    listJ.append(nextJ)

    #print("divisors"+str(divisors))
    for iteration in range(i):
        #print("iteration"+str(iteration))

        if iteration == 0:
            iterationResults.append((1/divisors[-1]) * c * listJ[-1])
        else:
            divisor = divisors[int(iteration-1)]
            fractionI = (1/((divisor**divisor)-1))
            last = iterationResults[-1]
            saved = listRes[-1][i-2]
            iterationResults.append(fractionI*(((divisor ** divisor) * last) - saved))
    listRes.append(iterationResults)
            


i = 2
siguiente(i)
#print(listRes)
decimal = int(input("cantidad de decimales: "))
#leemos la cantidad de decimales 
while error(listRes[-1][-2],listRes[-1][-1]) > (10**(-decimal)):
    i = i + 1
    siguiente(i)
    #print(listRes[-1])

for x in listRes:
    for y in x:
        print(y,end = " ")
    print()
