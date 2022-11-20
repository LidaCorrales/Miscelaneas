"""Omar Iván Trejos Buriticá, L. E. M. G. (2020). Introducción a la programación con Python.
Ediciones de la U. https://www-ebooks7-24-com.bdigital.sena.edu.co/?il=11870
Pagina digital: 36 - Taller de repaso"""

#Construir un programa que lea un número entero y determine si es un número positivo de 4 dígitos
num1 = int(input("Ingresar numero: "))

if num1 >= 1000 and num1 <= 9999:
    print(num1, "Es un numero de 4 digitos")
else:
    print(num1, "No es un numero de 4 digitos")