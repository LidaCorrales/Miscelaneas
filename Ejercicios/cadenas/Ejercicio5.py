#225, 233, 237, 243, 250
def acento(c):
    if(c[-1]==chr(225) or c[-1]==(233) or c[-1]==(237) or c[-1]==(243) or c[-1]==(250)):
        print("Es aguda")
    else:
        print("No es aguda")

acento('café')