#Ordenar el arreglo, de mayor a menor y de menor a mayor (algoritmo de la burbuja)
import random
random1=[]
rango = random.randint(10,25)
long = len(random1)

for i in range (rango):
    random1.append(round(random.random()*100))
print("Original: ", random1)
Intercambio = True
while Intercambio:
    Intercambio = False
    for i in range(len(random1)-1):
        if random1[i] > random1[i+1]:
            random1[i], random1[i+1] = random1[i+1], random1[i]
            Intercambio = True
print("Lista ordenada: ", random1)