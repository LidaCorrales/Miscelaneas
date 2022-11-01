#Solicitar 2 números al usuario e imprimir el cociente y el residuo del mayor en el menor 
dividendo1 = int(input("Escriba el dividendo: "))
divisor = int(input("Escriba el divisor: "))

if dividendo1 % divisor == 0:
    print("La división es exacta. Cociente :", (divisor // dividendo1))
else:
    print("La división no es exacta. Cociente: ", (divisor % dividendo1))