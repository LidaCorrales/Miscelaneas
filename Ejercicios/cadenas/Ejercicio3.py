#cuantas veces se repite un caracter dado

def caracter(cadena,suma):
    suma=[]
    for i in cadena:
        if i == searchcaracter:
            suma.append(i)
    return len(suma)
        

cadena = input("Ingresa una cadena: ")
searchcaracter = input("Ingresar la palabra a buscar: ")
print("El caracter", searchcaracter, "esta repetido", caracter(cadena,searchcaracter))