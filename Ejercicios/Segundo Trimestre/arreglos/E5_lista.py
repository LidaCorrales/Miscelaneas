#Solicite al usuario un número para buscar en la lista.
#Diga cuantas veces está y en que posiciones esta. Si no está agréguelo al final de la lista.
import random
from turtle import position
random1=[]
rango = random.randint(10,25)
contador = 0
posicion = ""
for i in range(rango):
    random1.append(round(random.random()*100))
print(random1)

numero = int(input("Escribir numero: "))
for i in range(rango):
    if numero == random1[i]:
        posicion+=str(i)
        contador+=1
if contador == 0:
    random1.append(numero)
    print("Se agrego al final de la lista")
    print(random1)
else:
    if contador == 1:
        print("El numero", numero, "esta 1 vez y esta en la posicion", position)
    else:
        print("El numero: ", numero, "esta", contador, "veces en la posicion", position)