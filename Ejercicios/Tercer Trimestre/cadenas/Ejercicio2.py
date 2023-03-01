#Pida una cadena por teclado y diga cual es su valor al sumar sus codigos
#Cual es el valor numerico de acuerdo a los códigos del alfabeto

def numerico (cod):
    suma=[]
    for letra in cod:
        suma.append(ord(letra))
    print("Codigos de la cadena", suma)
    suma2 = 0
    for i in suma:
        suma2+=i
    print("La suma de los codigos es:", suma2)

cod = input("Ingrese un valor: ")
numerico(cod)