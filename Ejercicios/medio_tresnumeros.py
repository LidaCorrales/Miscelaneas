#Encontrar el medio de tres numeros
A = int(input("Escribir el primer numero: "))
B = int(input("Escribir el segundo numero: "))
C = int(input("Escribir el tercer numero: "))

menor = min(A, B, C)
mayor = max(A, B, C)
medio = (A + B + C) - menor - mayor

print(menor, medio, mayor)
print("El numero del medio es: ", medio)