#De cada elemento de la lista diga si el elemento está por
# encima del promedio, debajo del promedio o es igual al promedio de todos los números de la lista.
import random
random1=[]
rango= random.randint(10,25)
suma = 0
promedio = 0
cont = 0
for i in range(rango):
    random1.append(round(random.random()*100))
    suma+=random1[i]
    promedio = suma // rango
print("La lista es ", random1)
print("El promedio es: ", promedio)
for n in random1:
    if n < promedio:
        print("El numero ", n, "es menor al promedio")
    elif n > promedio:
        print("El numero ", n, "es mayor al promedio")
    elif n == promedio:
        print("El numero ", n, "es igual al promedio")
