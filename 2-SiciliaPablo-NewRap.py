from sympy import *
from math import *

print("bienvenido al metodo de Newton Rapson")

listCoef = []
listRes = []
maxCoef = int(input("ingrese la potencia maxima de su ecuacion: "))
i = 0
while i <= (maxCoef):
    listCoef.append(float(input("ingrese la el coeficiente de X a la potencia " + str(maxCoef-i) + " en decimal: " )))
    i = i + 1

print(listCoef)

def funcion(x):
    res = 4*(x**3) - 12*(x**2) - x + 16
    return res
def derivada(x):
    res = 12*(x**2) -24*x -1
    return res 

def siguiente(x):
    sig = x-(funcion(x)/derivada(x))
    return sig

def error(x,y):
    relativeE = abs((y-x)/y)
    return relativeE
listRes.append(-1.5)
decimal = int(input("cantidad de decimales: "))
listRes.append(siguiente(listRes[-1]))

while error(listRes[-1], listRes[-2]) > (10**(-decimal)):
    listRes.append(siguiente(listRes[-1]))
    i = i + 1
    print(listRes)
    print(" converge a "+ str(decimal) +" decimales en "+ str(round(listRes[-1],decimal)) +" con "+ str(i) + " iteraciones" )

"""
listX = [] #lista de X 
ecuacion = input("ingrese el despeje de su ecuacion")

listX.append(float(input("ingresa un valor: ")))
decimal = int(input("cantidad de decimales: "))

class NoConverge(Exception):
    pass

def fun(x):
    result = eval(ecuacion)
    return result
    



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
"""