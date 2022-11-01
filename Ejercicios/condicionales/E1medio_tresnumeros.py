#Pedir 3 numeros e indicar cual de ellos es el valor del medio.
A = int(input("Escribir el primer numero: "))
B = int(input("Escribir el segundo numero: ")) #se piden los tres numeros por teclado
C = int(input("Escribir el tercer numero: "))

if A <= B <= C or C <= B <= A:
    print("El numero del medio es: ", B)
elif B < A < C or C < A < B:
    print("El numero del medio es ", A)
elif A < C < B or B < C < A:
    print("El numero del medio es: ", C)