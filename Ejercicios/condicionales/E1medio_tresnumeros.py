#Encontrar el medio de tres numeros
A = int(input("Escribir el primer numero: "))
B = int(input("Escribir el segundo numero: "))
C = int(input("Escribir el tercer numero: "))

if A <= B <= C or C <= B <= A:
    print("El numero del medio es: ", B)
elif B < A < C or C < A < B:
    print("El numero del medio es ", A)
elif A < C < B or B < C < A:
    print("El numero del medio es: ", C)