"""Omar Iván Trejos Buriticá, L. E. M. G. (2020). Introducción a la programación con Python.
Ediciones de la U. https://www-ebooks7-24-com.bdigital.sena.edu.co/?il=11870
Pagina digital: 36 - Taller de repaso"""

#Construir un programa que lea un número entero y determine si el resultado de 
#sumar sus dos últimos dígitos es un número de 1 dígito.

numero1 = int(input("Ingresar el numero: "))
num1 = int(str(numero1)[-1])
num2 = int(str(numero1)[-2])
resultado = num1+num2
print(num1, num2)
print(resultado)

if resultado >=0 and resultado <= 9:
    print("El numero es de 1 digito")
else:
    print("El numero no es de 1 digito")