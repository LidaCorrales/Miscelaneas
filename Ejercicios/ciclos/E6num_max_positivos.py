#Calcular el máximo de números positivos introducidos por teclado,el programa termina cuando se pone un numero negativo
numero = 0
c = 0

while(numero >= 0):
    numero = int(input("Introducir numeros: "))
    if numero >= 0:
        c+=1
    else:
        print("Numeros positivos registrados", c)