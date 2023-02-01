#3. se necesita un programa que permita ingresar 3 números y que muestre en la salida cuales son
#iguales y cuáles no.

def iguales(numero1,numero2,numero3):
    if numero1==numero2==numero3:
        print("Son iguales")
    elif numero1==numero2!=numero3:
        print("Dos son iguales y uno diferente")
    elif numero1!=numero2==numero3:
        print("uno es diferente y dos son iguales")
    else:
        print("Todos son diferentes")

numero1=int(input("Ingrese el primer numero:"))
numero2=int(input("Ingrese el segundo numero:"))
numero3=int(input("Ingrese el tercer numero:"))
iguales(numero1,numero2,numero3)