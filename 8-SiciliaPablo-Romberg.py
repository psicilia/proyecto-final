from sympy import *
from math import *

x = symbols('x')
print("bienvenido al metodo de Romberg")

listRes = []

ecuacion = input("ingrese su ecuacion: ")
y = eval(ecuacion)
a = float(input("ingrese el valor menor del intervalo: "))
b = float(input("ingrese el valor mayor del intervalo: "))
c = (b-a)
def error(a,b):
    relativeE = abs((b-a)/b)
    return relativeE

listRes.append(float((y.subs(x,a) + y.subs(x,b))/2))
i=2
print(listRes)


"""while i <= 16:
    j = 1
    while j < i:
        print(str(i)+"/"+ str(j))
        j = j + 2
    i = i * 2"""

def siguiente(k):
    j = 1
    sumF = 0
    while j < k:
        fract = a + (c * (j/k))
        sumF = sumF + y.subs(x,fract)
        #print(str(j)+"/"+str(k))
        j = j + 2
    listRes.append(listRes[-1] + sumF)

i = 2
  
siguiente(i)
decimal = int(input("cantidad de decimales: "))
while error(listRes[-1],listRes[-2]) > (10**(-decimal)):
    siguiente(i)
    print(listRes[-1])
    i = i * 2

print(listRes)

"""
while i <= :
    listX.append(a + (i*c))
    listRes.append(y.subs(x,listX[-1]))
    i = i +1""" 


