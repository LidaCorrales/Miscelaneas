#Solicitar 2 números al usuario e imprimir el cociente y el residuo del mayor en el menor sin utilizar
def main():
    print("DIVISOR DE NÚMEROS")
    dividendo1 = int(input("Escriba el dividendo-> "))
    divisor = int(input("Escriba el divisor->"))

    if dividendo1 % divisor == 0:
        print(f"La división es exacta. Cociente : {divisor // dividendo1}")
    else:
        print(
            f"La división no es exacta. Cociente: {divisor // dividendo1} "
            f"Resto: {dividendo1 % divisor}"
        )


if __name__ == "__main__":
    main()