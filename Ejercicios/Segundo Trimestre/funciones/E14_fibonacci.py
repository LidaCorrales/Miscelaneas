#Llene una lista con la serie de Fibonacci. La cantidad de elementos de la lista la debe
# ingresar el usuario. Mínimo debe tener 5 elementos y máximo 20.
# Ciclos
import random
def fibonacci(vec):
    print("tamaño", tam)
    for i in range(2,tam):
        vec.append(vec[i-1]+vec[i-2])
    return vec

vec = [0,1]
tam = round(random.randint(10,25))

print(fibonacci(vec))