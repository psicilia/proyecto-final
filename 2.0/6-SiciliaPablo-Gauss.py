"""
NAME 
   6-SiciliaPablo-Gauss.py

VERSION
  1.2

AUTHOR
  Pablo Sicilia Andrade  <psicilia@gmail.com>


DESCRIPTION
    programa que resuelve un sistema de ecuaciones lineales
    por el metodo numerico de Gauss-Seidel

CATEGORY
    metodos numericos
    Sistemas de ecuaciones lineales
USAGE
  6-SiciliaPablo-Gauss.py

GITHUB
    https://github.com/psicilia/proyecto-final/blob/966bcafc1ab154f1d427a45db73828d8c20c36a7/2.0/6-SiciliaPablo-Gauss.py

"""
import matplotlib.pyplot as plt
from math import *
import numpy as np
from sympy import *
import sympy as sp

print("bienvenido al metodo de Gauss Seidel")

variables = int(input("ingrese la cantidad de variables: "))

listMat = []
# lista de elementos de matriz 
listRes = []
#lista de resultados
listVar = []
# lista de variables

i = 0
for i in range(variables):
    ecuacion = "[" + input("ingrese los coeficientes de la ecuacion " + str(i+1) + " separados por comas: ") + "]"
    listMat.append(eval(ecuacion[:]))
    #leemos los renglones de la matriz 

def error(a,b):
    relativeE = abs((b-a)/b)
    return relativeE
    # definimos el calculo del error relativo

i = 0
for i in range(variables):
    listVar.append(0.0)
    # inicializamos la lista de variables

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
                    # cuando llegamos al termino independiente lo sumamos multiplicamos por -1 los demas elemntos
            j = j + 1
    
        listVar[i] = ((acum)/listMat[i][i])
        #agregamos a una lista los despejes de las variables
        i = i + 1
    listRes.append(listVar[:])

calcIter()

decimal = int(input("cantidad de decimales: "))
while error(listRes[-2][0], listRes[-1][0]) > (10**(-decimal)):
    #seguimos calculando si el error es menor al intervalo 
    calcIter()
print(listRes[-1])