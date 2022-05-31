"""
NAME 
   7-SiciliaPablo-Simpson.py

VERSION
  1.1

AUTHOR
  Pablo Sicilia Andrade  <psicilia@gmail.com>


DESCRIPTION
    programa que realiza una integracion numerica
    por el metodo numerico de simpson 1/3

CATEGORY
    metodos numericos
    integracion numerica

USAGE
  7-SiciliaPablo-Simpson.py

GITHUB
    https://github.com/psicilia/proyecto-final/blob/1cd01347085aaec9103a22486dc79181ab3a8702/7-SiciliaPablo-Simpson.py


"""
import matplotlib.pyplot as plt
from math import *
import numpy as np
from sympy import *
import sympy as sp

x = sp.Symbol('x')
# definimos x como simbolo
print("bienvenido al metodo de simpson")

listX = []
# lista de elemntos de X
listRes = []
# lista de resultados
i = 0

ecuacion = input("ingrese su ecuacion: ")
y = eval(ecuacion)
#leemos la ecuacion 
a = float(eval(input("ingrese el valor menor del intervalo: ")))
b = float(eval(input("ingrese el valor mayor del intervalo: ")))
n = int(eval(input("ingrese el valor de n: ")))
#leemos el intervalo y el valor de n

deltax = (b-a)/n
#definimos delta X con al dividir el intervalo entre n 
while i <= n:
    listX.append(a + (i*deltax))
    listRes.append(y.subs(x,listX[-1]))
    i = i + 1

sumPar = 0
sumImp = 0
for res in listRes[2:-2:2]:
    sumPar = sumPar + ((2) * (res))
    # seleccionamos los pares de la lista de resultados 
for res in listRes[1:-2:2]:
    sumImp = sumImp + res
    #seleccionamos los inpares de la lista de resultados 

result = (deltax/3)*(listRes[0] + listRes[-1] + (sumPar) + (4*sumImp))
# imprimimos el resultado final

x = np.linspace(a, b, 100)

funcion = eval(str(y))
print('y', type(y))
plt.bar(listX, listRes, color = 'r', width = deltax)
plt.plot(x, funcion, color= 'b')
plt.xlabel('x')
plt.ylabel('y')
plt.title(y)
plt.xticks(listX)
plt.show()