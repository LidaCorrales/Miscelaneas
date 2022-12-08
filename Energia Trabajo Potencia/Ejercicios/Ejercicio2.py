#Potencia
# Una grua eleva un bloque de 50 kg a una altura de 8 metros en 4 segundos

#Calcular trabajo de la grua
import math
def trabajo2():
    resultado =  peso*9.8*altura
    return resultado

peso = int(input("Ingresar peso del bloque: "))
altura = int(input("Ingresar altura de la grua: "))
solucion = trabajo2()
print(trabajo2(),"Jules")

#Calcular potencia en kw
def potencia(ecuacion):
    ecuacion = solucion/tiempo*(1/1000)
    return ecuacion

tiempo = int(input("Ingresar tiempo de subida: "))
p = potencia
print(potencia(p), "Kw")