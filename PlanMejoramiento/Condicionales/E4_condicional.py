"""Omar Iván Trejos Buriticá, L. E. M. G. (2020). Introducción a la programación con Python.
Ediciones de la U. https://www-ebooks7-24-com.bdigital.sena.edu.co/?il=11870
Pagina digital: 36 - Taller de repaso"""

#Construir un programa que lea un número entero y determine si su último dígito es un dígito par o impar.
numero1 = int(input("Ingresar el numero: "))
num1 = int(str(numero1)[-1])

if num1 %2==0:
    print(num1, "es un numero par")
else:
    print(num1, "es un numero impar")