#2. se requiere un programa que compare dos listas y diga cual tiene más elementos.
import random

def Listas(lista1,lista2):
    if lista1>lista2:
        print(lista1, "La primera lista tiene mas elementos")
    elif lista1<lista2:
        print(lista2, "La segunda lista tiene mas elementos")

lista1=[]
rango= random.randint(5,10)
for i in range (rango):
    lista1.append(round(random.random()*100))
lista2=[]
rango= random.randint(4,10)
for i in range (rango):
    lista2.append(round(random.random()*100))
Listas(lista1,lista2)