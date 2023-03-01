#Imprima todas las subcadenas que salen de una cadena comenzando con las dos primeras letras,
#luego tres primeras y así sucesivamente hasta llegar a la última
def sub_c(cad):
    letra=''
    for i in cad:
        letra+=i
        print(letra)


cadena=input('Ingrese una frase xd: ')
sub_c(cadena)