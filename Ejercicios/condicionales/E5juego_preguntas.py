# En un juego de preguntas a las que se responde “Si” o “No” gana quien responda correctamente las tres preguntas.
for i in range (1):
    primera_pregunta = input("¿Colon descubrio America?")
    if primera_pregunta != "si":
        break
    segunda = input("¿La Independencia de Colombia fue en el año 1810?")
    if segunda != "si":
        break
    tercera = input("¿The Doors fue un grupo de rock americamo?")
    if tercera != "si":
        break

    print("Respondio de manera correcta")