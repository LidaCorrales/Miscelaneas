#Pedir 3 numeros e indicar cual de ellos es el valor del medio. - Condicionales
def medio_tresnumeros(A,B,C):
    if A <= B <= C or C <= B <= A:
        print("El numero del medio es: ", B)
    elif B < A < C or C < A < B:
        print("El numero del medio es ", A)
    elif A < C < B or B < C < A:
        print("El numero del medio es: ", C)

    return medio_tresnumeros

print(medio_tresnumeros(4,9,6))