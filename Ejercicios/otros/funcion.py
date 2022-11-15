"""#si el numero es par o impar
import random
def parimpar(num):
    if num%2==0:
        #print("Par")
        return "Par"
    else:
        #print("Impar")
        return "Impar"

lista=[]
for i in range(10):
    lista.append(round(random.randrange(100)))
print(lista)
for i in lista:
    print(i)
    print (parimpar(i))"""

#suma de los divisores
def sumaDivisores(num):
    num=0
    for i in range(10):
        num+=1
        return num

#numeros amigos
def amigos(x, y):
    for i in range(1, amigos):
        sumx=sumaDivisores(x)
        sumy=sumaDivisores(y)
        if sumx==y and sumy==x:
            return "Son amigos"
        else:
            return "No son amigos"

print(sumaDivisores(10))
print(amigos(220,284))