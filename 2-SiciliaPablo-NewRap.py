import sympy as sp
from math import *

x = sp.Symbol('x')
print("bienvenido al metodo de Newton Rapson")

listCoef = []
listRes = []
maxCoef = int(input("ingrese la potencia maxima de su ecuacion: "))
i = 0
eq = ""
while i <= (maxCoef):
    listCoef.append(float(input("ingrese el coeficiente de X a la potencia " + str(maxCoef-i) + " en decimal: " )))
    if maxCoef-i == 0:
        eq = eq + str(listCoef[-1])
    else:
        eq = eq + str(listCoef[-1]) + (' * (x**')+ str(maxCoef-i) + ") + "
    i = i + 1

print(eq)
y = eval(eq)

def error(a,b):
    relativeE = abs((b-a)/b)
    return relativeE
    
derivada = y.diff(x)

def siguiente():
    aprox = (x-(y/derivada))
    return aprox.subs(x, (listRes[-1]))

decimal = int(input("cantidad de decimales: "))
listRes.append(float(input("ingrese valor inicial")))
listRes.append(siguiente())
print(listRes)
i = 1
while error(listRes[-1], listRes[-2]) > (10**(-decimal)):
    listRes.append(siguiente())
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