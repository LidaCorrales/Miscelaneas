#Detetrminar que tipo de palabra es: aguda, grave, esdrujula sobre esdrujula
#225, 233, 237, 243, 250
def aguda(c):
    if(c[-1]==chr(225) or c[-1]==chr(233) or c[-1]==chr(237) or c[-1]==chr(243) or c[-1]==chr(250)):
        print("Es aguda")
    elif(c[-2]==chr(225) or c[-2]==chr(233) or c[-2]==chr(237) or c[-2]==chr(243) or c[-2]==chr(250)):
        print('Es aguda')
    else:
        print("No es aguda")
def grave(c):
    if (c[-3]==chr(225) or c[-3]==chr(233) or c[-3]==chr(237) or c[-3]==chr(243) or c[-3]==chr(250)):
        print('Es grave')
    elif (c[-4]==chr(225) or c[-5]==chr(233) or c[-5]==chr(237) or c[-5]==chr(243) or c[-5]==chr(250)):
        print('Es grave')
    else:
        print("No es grave")
def esdrujula(c):
    if (c[-5]==chr(225) or c[-5]==chr(233) or c[-5]==chr(237) or c[-5]==chr(243) or c[-5]==chr(250)):
        print('Es esdrujula')
    elif (c[-6]==chr(225) or c[-6]==chr(233) or c[-6]==chr(237) or c[-6]==chr(243) or c[-6]==chr(250)):
        print("Es esdrujula")
    else:
        print("No es esdrujula")
def sobre_esdrujula(c):
    if (c[1] == chr(225) or c[1]==chr(233) or c[1]==chr(237) or c[1]==chr(243) or c[1]==chr(250)):
        print('Es sobreesdrujula')
    elif (c[2] == chr(225) or c[2]==chr(233) or c[2]==chr(237) or c[2]==chr(243) or c[2]==chr(250)):
        print('Es sobreesdrujula')
    elif (c[3] == chr(225) or c[3]==chr(233) or c[3]==chr(237) or c[3]==chr(243) or c[3]==chr(250)):
        print('Es sobreesdrujula')
    else:
        print("No es sobresdrujula")

oracion= input("Ingresar la palabra:")
grave(oracion)


