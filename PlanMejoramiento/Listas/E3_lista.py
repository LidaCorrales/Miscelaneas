"""Gaddis, T. (2015). Starting out with Python. Pearson
Educación. https://www-ebooks7-24-com.bdigital.sena.edu.co/?il=7498
Pagina digital: 318"""

#ubicar un nuevo numero en una posicion especifica
numbers = [1, 2, 3, 4, 5]   
numbers[2] = 99   
print(numbers)
#mostrar la posicion de un valor en una lista
numbers = [1, 2, 3, 4, 5]   
print(numbers[-2])
#mostrar los numeros de la lista comprendidos en el rango
numbers = list(range(1, 10, 2))   
for n in numbers:       
    print(n)