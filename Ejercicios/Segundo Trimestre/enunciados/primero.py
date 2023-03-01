#1.Solicitar 2 números al usuario e imprimir el cociente y el residuo del mayor en el menor.

def Cociente (numero1,numero2):
    cociente= numero1//numero2
    residuo= numero1 % numero2
    print("El cociente del numero es", cociente, "y el residuo es: ",residuo)

numero1 = int(input("Ingrese el primer numero:"))
numero2 = int(input("Ingrese el primer numero:"))
Cociente(numero1,numero2)