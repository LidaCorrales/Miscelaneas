#Llene una lista con la serie de Fibonacci. La cantidad de elementos de la lista la debe
# ingresar el usuario. Mínimo debe tener 5 elementos y máximo 20.
import random
random1 = []
aux = True
A = 0
B = 1
C = 1
while aux:
    rango = int(input("Cantidad de elementos a ejecutar en la serie: "))
    if rango >= 5 and rango <=20:
        aux=False
    else:
        print("Deben ser minimo 5 elementos y maximo 20")
    
for i in range(rango):
    C = A + B
    A = B
    B = C
    random1.append(C)
print("La lista con los valores de Fibonacci hasta la posicion insertada es: ", random1)