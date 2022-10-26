#pedir numeros, imprimirlo con el opuesto, finaliza con cero y diga cuantos ingreso

n = 1
cont = 0

while True:
    n = int(input("Ingresar un numero: "))
    contrario = n*-1
    if n==0:
        print("Numeros puestos: ", cont)
        break
    elif n>0:
        print("El numero es", n, "el contrario es: ", contrario)
    else:
        print("El numero", n, "y su contrario: ", contrario)
    cont+=1