#Determinar los divisores de un número introducido por teclado - Ciclos
def divisores(numero):
    contador = 1
    print("Los divisores son: ")
    while(numero >= contador):
        if numero%contador == 0:
            print(contador)
        contador+=1
    return numero

print(divisores(98))