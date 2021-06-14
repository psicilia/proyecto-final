from sympy import *
from math import *

print("bienvenido al metodo de aproximaciones sucesivas")

listX = [] #lista de X 
ecuacion = input("ingrese el despeje de su ecuacion")
listX.append(float(input("ingresa un valor: ")))
decimal = int(input("cantidad de decimales: "))

class NoConverge(Exception):
    pass

def fun(x):
    result = eval(ecuacion)
    return result
    

def error(x,y):
    relativeE = abs((y-x)/y)
    return relativeE

i = 1
listX.append(fun(listX[-1]))
try:
    while error(listX[-1], listX[-2]) > (10**(-decimal)):
        listX.append(fun(listX[-1]))
        i = i + 1
        if not type(listX[-1]) is float:
            raise NoConverge
except ZeroDivisionError:
    print("no es posible dividir entre 0")
except NoConverge:
    print("no converge con el valor de x aproximado")
else: 
    print(listX)
    print(" converge a "+ str(decimal) +" decimales en "+ str(round(listX[-1],decimal)) +" con "+ str(i) + " iteraciones" )
