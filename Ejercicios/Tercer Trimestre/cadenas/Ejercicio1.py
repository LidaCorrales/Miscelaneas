#Cuantas letras del abecedario estan en la cadena, si estan repetidas cuentela solo una vez

ab = 'aaaabbcdefghijklmnopqrstuvwxyz'
def Abecedario (cadena):
    suma =[]
    for letra in cadena:
        if letra not in suma:
            suma.append(letra)
    return len(suma)

print("Cantidad de letras en el abecedario: ", Abecedario(ab))

