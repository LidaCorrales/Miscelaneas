#Encuentre la suma y el promedio de los números de la lista
import random 
random1=[]
rango= random.randint(10,25)
suma = 0
promedio = 0
contador = 0

for i in range (rango):
    random1.append(round(random.random()*100))
    suma+=random1[i]
    contador+=1
    promedio=suma//contador
print(random1)
print("La suma es: ", suma)
print("El promedio es: ", promedio)