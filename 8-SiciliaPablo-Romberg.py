from sympy import *
from math import *

x = symbols('x')
print("bienvenido al metodo de Romberg")

listRes = []
listJ = []

ecuacion = input("ingrese su ecuacion: ")
y = eval(ecuacion)
#leemos la ecuacion
a = float(input("ingrese el valor menor del intervalo: "))
b = float(input("ingrese el valor mayor del intervalo: "))
c = (b-a)
#definimos el intervalo 

def error(a,b):
    relativeE = abs((b-a)/b)
    return relativeE
    #definimos la operacion para calcular el error relativo

listJ.append((y.subs(x,a) + y.subs(x,b))/2)
# definimos J1 

listRes.insert(0, float(c*listJ[0]))
#calculamos I1 
print(listRes)
#imprimimos I1

def siguiente(i):
    iterationResults = []
    for iteration in range(i):
        if iteration > 10:
            iterationResults.append(int(10))
        else:   
            iterationResults.append(int(iteration+1))
    listRes.append(iterationResults)


i = 2
siguiente(i)
print(listRes)
decimal = int(input("cantidad de decimales: "))
#leemos la cantidad de decimales 
while error(listRes[-1][-2],listRes[-1][-1]) > (10**(-decimal)):
    i = i + 1
    siguiente(i)
    print(listRes[-1])

print(listRes)

