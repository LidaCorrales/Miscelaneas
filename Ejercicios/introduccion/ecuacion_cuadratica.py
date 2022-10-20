A = 0
B = 0
C = 0
Z = 0

numero = input("¿Obtener valor de A?")
if numero == "si":
    A = int(input("Ingresar valor de A: "))
numero = input("¿Obtener valor de B?: ")
if numero == "Si":
    B = int(input("Ingresar valor de B: "))
numero = input("¿Obtener valor C?")
if numero == "si":
    C = int(input("Ingrese el valor de C: "))
numero = input("¿Obtener el valor de X?")
if numero == "Si":
    X = int(input("Ingresar valor de X: "))

Formula = (A*(X**2)) + (B*X) + C
print("La funcion cuadratica es: ", Formula)