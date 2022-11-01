#Algoritmo para hallar el m.c.d de dos números m y n por el algoritmo de Euclides.
n = int(input("Introducir el primer numero: "))
m = int(input("Introduzca el segundo numero: "))

while not (m == 0):
    a=n
    b=m
    if n < 0:
        n-=a
        m=b
    if m < 0:
        n=a
        m=-b
    else:
        n=b
        m= a%b
print(n)