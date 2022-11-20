"""Hinojosa Gutiérrez, A. P. (2016). Python: paso a paso. Ediciones de la U..
 https://www-ebooks7-24-com.bdigital.sena.edu.co/?il=7959
 Pagina digital 78"""

lista = ["primero", "segundo", "tercero", "cuarto", "quinto", "sexto"]
lista2 = lista[1:4]
print (lista2)
# Mostrará "['segundo', 'tercero', 'cuarto']"
lista2[0:2] = ["otro", "Y otro"]
print (lista2)
# Mostrará "['otro', 'Y otro', 'cuarto']"