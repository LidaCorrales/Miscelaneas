minutos = int(input("Ingrese los minutos de la llamama: "))
if minutos > 0: 
    if minutos <= 3:
        total = minutos*200
    elif minutos > 3:
        adicional = minutos*50
        total = minutos*adicional
print("El total a pagar es: ", total, "pesos")