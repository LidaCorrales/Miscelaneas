dirarchivo = "Ejemplo.txt"
while True:                                                                                     #Creamos un bucle infinito
    try:                                                                                        #Intentamos abrirlo
        with open (dirarchivo, "r+") as f:                                                      #Abrimos utilizando Reescribir (r+)
            contenido = f.read()                                                                #<-Lo abrimos utilizando el método read
            print (contenido)
            break
    except:
        print("Error al intentar abrir")
        print (("No se encuentra el archivo"),(dirarchivo), ("Especifique su ubicación:"))
        dirarchivo = (input("Dirección:"))