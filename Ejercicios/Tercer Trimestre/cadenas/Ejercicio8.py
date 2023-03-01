#Invente un cifrado de texto tipo murcielago o César. Puede utilizar alguna formula matemática para este fin.

def cifrado(cadena):
    cadena2 = ''
    for char in cadena:
        if not char.isalnum():
            continue
        char = char.upper()
        codigo = ord(char) + 3
        if codigo > ord('9'):
            codigo = ord('0')
        cadena2 += chr(codigo)
    print(cadena2)
    

cadena = input("Ingresa tu mensaje en numeros: ")
cifrado(cadena)