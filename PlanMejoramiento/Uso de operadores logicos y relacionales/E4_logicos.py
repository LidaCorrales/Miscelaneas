"""Omar Iván Trejos Buriticá, L. E. M. G. (2020). Introducción a la programación con Python.
 Ediciones de la U. https://www-ebooks7-24-com.bdigital.sena.edu.co/?il=11870
 Pagina digital: 28 - taller de repaso"""

#Construir un programa que reciba dos números y muestre la suma de sus tres últimos dígitos
numero1 = int(input("Ingresar numero: "))
numero2 = int(input("Ingresar segundo numero: "))

numero1 = int(str(numero1)[-3:])
numero2 = int(str(numero2)[-3:])
print(numero1,numero2)
resultado = numero1+numero2
print(resultado)