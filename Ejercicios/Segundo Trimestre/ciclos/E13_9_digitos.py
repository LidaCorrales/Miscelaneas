#Solicitar al usuario un número de hasta 9 dígitos e imprimirlo en orden contrario.
num = (input("Ingrese 9 digitos: "))

for i in range(len(num)-1,-1,-1):
    print((num[i]), end=("-"))