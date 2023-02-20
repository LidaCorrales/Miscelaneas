#De una cadena diga cuantas vocales tiene, cuantas consonantes, cuantas vocales 
#con tilde y cuantos caracteres especiales.

def caracteres(cadena):
    contador = 0
    for i in cadena:
        for c in range(ord(' '),ord('/')):
            if ord(i)==c:
                contador+=1
        print(contador)

def Mayusculas(cadena):
    contador = 0
    for i in cadena:
        for c in range(ord('A'),ord('Z')):
            if ord(i)==c:
                if ord(i)==65 or ord(i)==69 or ord(i)==73 or ord(i)==79 or ord(i)==85:
                    contador+=1
                else:
                    continue
    print(contador)

palabra=input("Ingrese una palabra:")
