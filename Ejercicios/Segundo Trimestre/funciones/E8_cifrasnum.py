#Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene. - Condicionales
def pedir_numeros(numero):
    if(numero <0 or numero>9999):
        print("El numero que ingreso es invalido")
    else:
        if(numero<10):
            print("El numero ingresado tiene 1 cifra")
        elif (numero<100):
            print("El numero ingresado tiene 2 cifras")
        elif(numero<1000):
            print("El numero ingresado tiene 3 cifras")
        elif(numero<9999):
            print("El numero ingresado tiene 4 cifras")

    return numero
print(pedir_numeros(78))
