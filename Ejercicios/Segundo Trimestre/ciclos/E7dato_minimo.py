#Encontrar un número natural n más pequeño tal que la suma de los n primeros números naturales
dato_max = int(input("Introducir dato maximo: "))
numero = 0
contador = 0
centi = True
suma = 0

while(suma < dato_max):
    numero+=1
    suma = 0
    for i in range(0, numero+1):
        suma+=i

print(numero, "es el numero natural minimo solicitado para superar el dato maximo")
