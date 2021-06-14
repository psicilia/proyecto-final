import decimal
from sympy import *
from math import *

print("bienvenido al metodo de aproximaciones sucesivas")

listX = [] #lista de X 
ecuacion = input("ingrese el despeje de su ecuacion")
listX.append(float(input("ingresa un valor: ")))
decimal = int(input("cantidad de decimales: "))
def fun(x):
    result = eval(ecuacion)
    #result = (cbrt(1-x))
    return result

def error(x,y):
    relativeE = abs((y-x)/y)
    return relativeE

i = 1
listX.append(fun(listX[-1]))
while error(listX[-1], listX[-2]) > (10**(-decimal)):
    if i > 3:
        pverror = error(listX[-2], listX[-3])
        if pverror < error(listX[-1], listX[-2]):
            print("no converge")
    listX.append(fun(listX[-1]))
    i = i + 1 

print(listX)
print(" converge a "+ str(decimal) +" decimales en "+ str(round(listX[-1],decimal)) +" con "+ str(i) + " iteraciones" )