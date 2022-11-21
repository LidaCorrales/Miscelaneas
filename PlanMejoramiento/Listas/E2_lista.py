"""Omar Iván Trejos Buriticá, L. E. M. G. (2020). Introducción a la programación con Python.
Ediciones de la U. https://www-ebooks7-24-com.bdigital.sena.edu.co/?il=11870
Pagina digital: 43"""

#Construir un programa que permita determinar si un valor escrito por el usuario,
# está o no está dentro de un conjunto de datos.
a = [1,2,3,4,5]                             # se almacena una lista de datos
r = False                                   # se inicia r con un valor 
b = int(input("Dato a buscar: "))           # se recibe el dato del usuario
for i in a:                                 #se plantea una búsqueda el dato del usuario dentro de la lista    
    if i == b:                              #si lo encuentra        
        print("Lo encontré")                #avisa que lo encontró        
        r = True                            # y pone r en Verdadero
if r == False:                              # al salir del ciclo, si r es Falso signica que no encontró el valor    
    print("No lo encontré")