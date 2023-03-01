#4.se necesita un programa el cual permite ingresar el nombre de un jugador famoso y este
#imprima el club al que pertenece.

def jugadores(jugador):
    if jugador == "messi":
        return("nose")
    elif jugador == "cristiano":
        return("zzz")
    elif jugador == "mbappe":
        return("Francia?")
    else:
        return("El nombre del jugador no se encuentra en la lista xd")

jugador= input("Ingrese el nombre del jugador:")
print(jugadores(jugador))
