#Hallar el trabajo
#Calcular el trabajo que realiza la fuerza F sobre la distancia d.
#Datos F = 15N Grados = 35 Distancia = 2

import math
def trabajo():
    resultado = Fuerza*(Desplazamiento*math.cos(Grados))
    return resultado

Fuerza = int(input("Ingresar la fuerza: "))
Desplazamiento = int(input("Ingresar el desplazamiento: "))
Grados = int(input("Ingresar los grados: "))
w = trabajo()
print(trabajo(), "Jules")