"""Omar Iván Trejos Buriticá, L. E. M. G. (2020). Introducción a la programación con Python.
Ediciones de la U. https://www-ebooks7-24-com.bdigital.sena.edu.co/?il=11870
Pagina digital: 36 - Taller de repaso"""

#Construir un programa que lea dos números enteros
#y determine si el 1er número leído es mayor que el 2º número leído.
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

if numero1 > numero2:
    print("El numero", numero1, "es mayor que", numero2)
elif numero1 == numero2:
    print("Los numeros son iguales")
else:
    print("El numero", numero1, "es menor que", numero2)