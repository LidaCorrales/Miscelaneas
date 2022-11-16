##Determinar cuales son los múltiplos de 5 - Ciclos
def multiplo(numero, multiplo):
    return numero % multiplo == 0

for i in range(31):
    print(i)
    if multiplo(i, 5):
        print("Sí es múltiplo")
    else:
        print("No es múltiplo")

print(multiplo(5, 2))