notas = int(input("Ingrese la nota de 0 a 10: "))

if (notas >= 0 and notas <5):
    print("Su nota es: Insuficiente")
elif(notas == 5):
    print("Su nota es: Aceptable")
elif(notas >5 and notas <=9):
    print("Su nota es: Sobresaliente")
elif(notas == 10):
    print("Su nota es: Excelente")
else:
    print("El valor no es correcto")