#Realizar un programa que determine esta fecha para un año ingresado por teclado.
año = int(input("Ingrese el año: "))

A = año % 19
B = año % 4
C = año % 7
D = (19*A+24) % 30
E = (2*B+4*C+6*D+5) % 7
N = (22+D+E)

if N > 31:
    N-=31
    print("La pascua fue el", N, "de Abril")
elif N <= 31:
    print("La pascua fue el", N, "de Marzo")
