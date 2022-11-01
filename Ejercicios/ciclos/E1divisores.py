#Determinar los divisores de un número introducido por teclado
numero = int(input("Escribir el numero: "))
contador = 1

print("Los divisores son: ")
while(numero >= contador):
    if numero%contador == 0:
        print(contador)
    contador+=1