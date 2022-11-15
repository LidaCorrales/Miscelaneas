##Comparador de tres numeros
def comparador(numero1, numero2, numero3):

    if numero1 == numero2 == numero3:        
        print("Ha escrito tres veces el mismo número.")
    elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3:        
        print("Ha escrito uno de los números dos veces.")
    else:        
        print("Los tres números que ha escrito son distintos.")

    return comparador

print(comparador(2, 2, 7))