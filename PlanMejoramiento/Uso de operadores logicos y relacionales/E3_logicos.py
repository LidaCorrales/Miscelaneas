"""Omar Iván Trejos Buriticá, L. E. M. G. (2020). Introducción a la programación con Python.
 Ediciones de la U. https://www-ebooks7-24-com.bdigital.sena.edu.co/?il=11870
 Pagina digital: 28 - taller de repaso"""

#Construir un programa que reciba un número entero y muestre el resultado de
#elevar su penúltimo dígito a la potencia representada por su último dígito
num1 = int(input("Ingresar primer numero: "))
num2 = int(input("Ingresar segundo numero: "))

num1 = int(str(num1)[-2])
num2 = int(str(num2)[-1])
print(num1,num2)
resultado_potencia = num1**num2
print(resultado_potencia)