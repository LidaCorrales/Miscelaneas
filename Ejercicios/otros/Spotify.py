listareproduccion = {"maluma": {
                                "Genero" : "Urbano",
                                "cancion" :"perdedor",
                                "duracion" : "3:27" 
                                }, 
                    "INTERWORLD" : {
                                "Genero" : "Phonk",
                                "cancion" : "METAMORPHOSIS",
                                "duracion" : "2:22"
                                 },
                    "Metallica" : {
                                "Genero" : "Rock",
                                "cancion": "Enter Sandman",
                                "duracion" : "5:31"
                                 },
                    "Canserbero" : {
                                "Genero": "Rap",
                                "cancion" : "Maquiavelico",
                                "duracion" : "4:44"
                                 },
                    "Luis Miguel" : {
                                "Genero": "Pop",
                                "cancion" : "Ahora te puedes marchar",
                                "duracion" : "3:11"
                                },
                    "Bad Bunny" : {
                                "Genero": "Urbano",
                                "cancion" : "NI BIEN NI MAL",
                                "duracion" : "3:56"
                                }
  }
print(listareproduccion ["maluma"]["cancion"])

def artista (artista, playlist):
    if artista in playlist:
        print(playlist[artista])
    else:
        print("El artista no se encuentra en la playlist")
#artista("maluma", listareproduccion)
x = str(input("Ingrese el artista:"))
artista(x,listareproduccion)

def agregar(playlist):
    x = input("artista")
    c = input("cancion")
    g = input("genero")
    d = input("duracion")
    playlist[x]={c, g, d}
    
    #playlist["artista"]=x
    #diccionario.update({artista: x})
    
agregar(listareproduccion)