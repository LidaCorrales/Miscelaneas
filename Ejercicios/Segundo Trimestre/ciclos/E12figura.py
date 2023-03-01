#Escribir un programa que visualice la siguiente figura, utilizando ciclos.
numero = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(numero):
    for j in range(i+1):
        print("*", end="")
    print("")