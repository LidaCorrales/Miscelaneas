"""Omar Iván Trejos Buriticá, L. E. M. G. (2020). Introducción a la programación con Python.
Ediciones de la U. https://www-ebooks7-24-com.bdigital.sena.edu.co/?il=11870
Pagina digital: 41"""

#De una frase digitada por el usuario, determinar cuántos espacios en blanco tiene:
cont = 0
frase = input("Introducir frase: ")

for i in frase:    
    if i == " ":
        cont = cont + 1
print("\n\nLa frase tiene", cont, "espacios")