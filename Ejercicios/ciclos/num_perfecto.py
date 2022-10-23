from re import I


numero = int(input("Ingrese el numero: "))

i = 1
total = 0
while (i<numero):
    if numero%1 == 0:
        total += i
    i+= 1

if total == 0:
    print("Perfecto")
else:
    print("No es numero perfecto")