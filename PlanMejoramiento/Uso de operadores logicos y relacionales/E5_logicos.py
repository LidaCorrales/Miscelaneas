"""Omar Iván Trejos Buriticá, L. E. M. G. (2020). Introducción a la programación con Python.
 Ediciones de la U. https://www-ebooks7-24-com.bdigital.sena.edu.co/?il=11870
 Pagina digital: 28 - taller de repaso"""

#Construir un programa que reciba un número entero y obtenga su mitad entera
numero = int(input("Introducir numero: "))

resultado = numero // 2
print(resultado)

#Operador logico
if resultado:
    numero % 2 == 0 or numero % 3 == 0
    print("el numero es divisible por 2 o 3")
else:
    print("Numero es 0")
"""es True si una de las dos condiciones es True, esto es, si el número n es divisible por 2 o es
divisible por 3"""