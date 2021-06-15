import sympy as sp
from math import *

x = sp.Symbol('x')
# definimos x como simbolo
print("bienvenido al metodo de Newton Rapson")

listEsc = []
# lista de coeficientes 
listRes = []
# lista de resultados
maxCoef = int(input("ingrese la potencia maxima de su ecuacion: "))
# leemos el valor de la potencia mas alta, para determinar la cantidad de terminos
i = 0
eq = ""
#inicializamos eq 
while i <= (maxCoef):
    listEsc.append(float(input("ingrese el escalar de X a la potencia " + str(maxCoef-i) + " en decimal: " )))
    # leemos los valores escalares para cada termino 
    if maxCoef-i == 0:
        eq = eq + str(listEsc[-1])
        # si es el ultimo termino no agregamos x ni un mas al final
    else:
        eq = eq + str(listEsc[-1]) + (' * (x**')+ str(maxCoef-i) + ") + "
    i = i + 1

print(eq)
# mostramos la ecuacion final
y = eval(eq)

def error(a,b):
    relativeE = abs((b-a)/b)
    return relativeE
    #definimos el calculo del error relativo
    
derivada = y.diff(x)
# derivamos y con respecto a x

def siguiente():
    aprox = (x-(y/derivada))
    return aprox.subs(x, (listRes[-1]))
    # definimos el calculo del siguiente resultado

decimal = int(input("cantidad de decimales: "))
listRes.append(float(input("ingrese valor inicial: ")))
#leemos la precision y el valor inicial
listRes.append(siguiente())
# calculamos el resultado calculando con el valor inicial
i = 1
while error(listRes[-1], listRes[-2]) > (10**(-decimal)):
    # si el error de los resultados es mayor al margen seguimos calculando 
    listRes.append(siguiente())
    i = i + 1
print(" converge a "+ str(decimal) +" decimales en "+ str(round(listRes[-1],decimal)) +" con "+ str(i) + " iteraciones" )