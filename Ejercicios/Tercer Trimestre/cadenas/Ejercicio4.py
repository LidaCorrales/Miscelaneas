#Solicite cadena e imprimala en todas las formas posibles en cuanto a mayusculas y minusculas

def MayMin():
    print(cadena.swapcase())
    print(cadena.title())
    print(cadena.capitalize())
    print(cadena.upper())
    print(cadena.lower())

cadena = input("Ingresar una cadena: ")
MayMin()