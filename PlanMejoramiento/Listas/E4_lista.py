"""Gaddis, T. (2015). Starting out with Python.
Pearson Educación. https://www-ebooks7-24-com.bdigital.sena.edu.co/?il=7498
Pagina digital: 354 - Programming Exercises"""

#Lottery Number Generator - Generador de numeros de loteria
#Design a program that generates a seven-digit lottery number. The program should generate seven random numbers,
#each in the range of 0 through 9, and assign each number to a list element.
#Then write another loop that displays the contents of the list.
import random

filas = 3
columnas= 7
valores = [[0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0]]
for i in range(filas):
    for c in range(columnas):
        valores[i][c] = random.randint(1,9)
#Imprimir valores
print("Los numeros de la loteria son:")
for x in valores:
    print(x)