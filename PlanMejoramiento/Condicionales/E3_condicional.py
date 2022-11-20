"""Omar Iván Trejos Buriticá, L. E. M. G. (2020). Introducción a la programación con Python.
Ediciones de la U. https://www-ebooks7-24-com.bdigital.sena.edu.co/?il=11870
Pagina digital: 36 - Taller de repaso"""

#Construir un programa que lea dos números enteros y determina si el último dígito del
#1er número leído es par y, al tiempo, si el penúltimo dígito del 2º número leído es impar.

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresar el segundo numero: "))

num1 = int(str(num1)[-1])
num2 = int(str(num2)[-2])

if num1 %2==0:
    print ("El primer numero:", num1, "es par")
    if num2 %2==0:
        print("El segundo numero es par")
    else:
        print("El segundo numero", num2, "es impar")
else:
    print("El primer numero no es par")