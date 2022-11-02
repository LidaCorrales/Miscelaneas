#Sume los pares y saque el promedio de los impares
import random 
random1=[]
rango= random.randint(10,25)
suma_pares = 0
suma_impares = 0
promedio_impares = 0
contador = 0
contador2 = 0
longitud = len(random1)

for i in range (rango):
    random1.append(round(random.random()*100))
    longitud = len(random1)
    if longitud%2 == 0:
        suma_pares+=random1[i]
        contador+=1
    if longitud%2 != 0:
        suma_impares+=random1[i]
        contador2+=1
        promedio_impares=suma_impares//contador2
print("La lista: ", random1)
print("La suma de los pares es: ", suma_pares)
print("El promedio de los impares es: ", promedio_impares)