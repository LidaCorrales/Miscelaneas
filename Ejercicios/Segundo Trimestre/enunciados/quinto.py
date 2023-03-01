#5.se requiere un programa que al ingresar el nombre y las horas trabajadas muestre su salario
#correspondiente.

def salario(nombre,hora:)
    h2 = hora - 40
    if hora < 40:
        hora *= 2600
        print("El salario semanal es: ", hora)
    elif hora > 40:
        hora = 40
        hora *= 2600
        h2 *= 5000
        print("El salario semanal es: ", hora + h2)

hora = int(input("Digite la cantidad de horas: "))