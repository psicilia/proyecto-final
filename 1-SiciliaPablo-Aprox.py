"""
NAME 
    1-SiciliaPablo-Aprox.py

VERSION
  1.1

AUTHOR
  Pablo Sicilia Andrade  <psicilia@gmail.com>


DESCRIPTION
    programa que aproxima la raiz de una ecuacion
    por el metodo numerico de Aproximaciones sucesivas

CATEGORY
    metodos numericos
    raices de ecuaciones

USAGE
  1-SiciliaPablo-Aprox.py

GITHUB


"""

from sympy import *
from math import *

print("bienvenido al metodo de aproximaciones sucesivas")

listX = [] #lista de valores de X 
ecuacion = input("ingrese el despeje de su ecuacion: ")
# leemos la ecuacion de teclado
listX.append(float(eval(input("ingresa un valor: "))))
# agregamos el valor inicial de x a la lista
decimal = int(input("cantidad de decimales: "))
# leemos la cantidad de decimales a utilizar

class NoConverge(Exception):
    pass
#definimos un error en caso de no convergencia

def fun(x):
    result = eval(ecuacion)
    return result
    #resolvemos para la x determinada
    

def error(x,y):
    relativeE = abs((y-x)/y)
    return relativeE
    #definimos el calculo del error relativo

i = 1
listX.append(fun(listX[-1]))
#obtenemos el valor de x1 
try:
    while error(listX[-1], listX[-2]) > (10**(-decimal)):
        # si el error entre xi+1 y xi es mayor que el margen continuamos 
        listX.append(fun(listX[-1]))
        i = i + 1
        if not type(listX[-1]) is float:
            #si el xi no es un numero flotante el metodo no converge
            raise NoConverge
except ZeroDivisionError:
    print("no es posible dividir entre 0")
    # detenemos en caso de devidir entre 0
except NoConverge:
    print("no converge con el valor de x aproximado")
else: 
    print(" converge a "+ str(decimal) +" decimales en "+ str(round(listX[-1],decimal)) +" con "+ str(i) + " iteraciones" )
    # mostramos el ultimo elemento calculado de la lista de x