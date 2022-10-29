from re import I


i = 1
contador = 0
suma = 0
numero = int(input("Ingrese el numero: "))

while (numero > i):
    if numero%i == 0:
        contador = i
    i+= 1

for i in range(contador + 1):
    suma+=1

if numero == suma:
    print(numero, "Es perfecto")
else:
    print(numero, "No es perfecto")