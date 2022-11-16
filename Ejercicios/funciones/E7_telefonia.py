#Telefónica realiza los cálculos del costo de una llamada de teléfono. - condicionales
tres_minutos=200
def minutos(minutos):
    if minutos <=3 and minutos > 0:
        print("La llamada costo 200")
    elif minutos > 3:
        minutos = ((minutos-3)*50)+200
        print("La llamada costo: ", minutos)
    else:
        print("El numero introducido no es correcto")
    return minutos

print(minutos(4))