from sympy import *
from math import *

x = symbols('x')
print("bienvenido al metodo de simpson")

listX = []
listRes = []
i = 0

ecuacion = input("ingrese su ecuacion: ")
y = eval(ecuacion)
a = float(input("ingrese el valor menor del intervalo: "))
b = float(input("ingrese el valor mayor del intervalo: "))
n = int(input("ingrese el valor de n: "))

deltax = (b-a)/n

while i <= n:
    listX.append(a + (i*deltax))
    listRes.append(y.subs(x,listX[-1]))
    i = i + 1

sumPar = 0
sumImp = 0
for res in listRes[2:-2:2]:
    sumPar = sumPar + ((2) * (res))
for res in listRes[1:-2:2]:
    sumImp = sumImp + res

result = (deltax/3)*(listRes[0] + listRes[-1] + (sumPar) + (4*sumImp))
print(result)
