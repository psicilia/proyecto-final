import sympy as sp
import numpy as np
from math import *

print("bienvenido al metodo de Gauss Seidel")

variables = int(input("ingrese la cantidad de variables: "))
#listMat = [[8,-1,2,10],[1,-9,1,-8],[3,1,-12,-12]]
listMat = []
listRes = []
listVar = []

i = 0
for i in range(variables):
    ecuacion = "[" + input("ingrese los coeficientes de la ecuacion " + str(i+1) + " separados por comas: ") + "]"
    listMat.append(eval(ecuacion[:]))

def error(a,b):
    relativeE = abs((b-a)/b)
    return relativeE

i = 0
for i in range(variables):
    listVar.append(0.0)

listRes.append(listVar[:])

def calcIter():
    i = 0
    for i in range(variables):
        acum = 0.0
        j = 0 
        for j in range(variables+1):
            if j != i:
                if j != variables:
                    acum = acum + (listMat[i][j] * listVar[j])
                else:
                    acum = (-acum + listMat[i][j]) 
            j = j + 1
    
        listVar[i] = ((acum)/listMat[i][i])
        i = i + 1
    listRes.append(listVar[:])

calcIter()
print(listRes)

print(listRes[-1][0])
print(listRes[-2][0])

decimal = int(input("cantidad de decimales: "))
while error(listRes[-2][0], listRes[-1][0]) > (10**(-decimal)):
    calcIter()
print(listRes[-1])