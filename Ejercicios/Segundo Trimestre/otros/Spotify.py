listareproduccion = {"maluma": (
                                "Genero" "Urbano",
                                "cancion" "perdedor",
                                "duracion" "3:27" 
                                ), 
                    "INTERWORLD" : (
                                "Genero" "Phonk",
                                "cancion" "METAMORPHOSIS",
                                "duracion" "2:22"
                                ),
                    "Metallica" : (
                                "Genero" "Rock",
                                "cancion" "Enter Sandman",
                                "duracion" "5:31"
                                 ),
                    "Canserbero" : (
                                "Genero" "Rap",
                                "cancion" "Maquiavelico",
                                "duracion" "4:44"
                                  ),
                    "Luis Miguel" : (
                                "Genero" "Pop",
                                "cancion" "Ahora te puedes marchar",
                                "duracion" "3:11"
                                ),
                    "Bad Bunny" : (
                                "Genero" "Urbano",
                                "cancion" "NI BIEN NI MAL",
                                "duracion" "3:56"
                                  )
                                  }
print(listareproduccion ["maluma"]["cancion"])

#funcion buscar
def artista (playlist):
    artista1 = input("Nombre del cantante que quieres buscar: ")
    if artista1 in playlist:
        print(playlist[artista1])
    else:
        print("El artista no se encuenta")

#funcion agregar artitas
def agregarArtista(playlist):
        y=input("Escribe el nombre del artista que quieres agregar\n")
        playlist[y]=()
        print(playlist)
        return 1

#Agregar cancion
def agregarCancion (playlist):
    artisca2=input("Nombre del artista al que le quieres agregar una cancion:\n")
    c=input("Nombre de la cancion que quieres agregar:\n")
    g=input("genero de la cancion:\n")
    d=input("duracion de la cancion:\n")
    dicci=("cancion", c,"duracion", d,"genero", g)
    playlist[artisca2]+=dicci
    print(playlist)

#Eliminar artista
def eliminarArtista(playlist):
    eliminar=input("Nombre del artista que quieres eliminar\n")
    del playlist[eliminar]
    print(playlist)

#organizar playlist
def ordenarLista(playlist):
    sorted((playlist.keys()))
    print(playlist)

#Menu
while True:
    print("1-Buscar artista")
    print("2-Agregar artista")
    print("3-Agregar cancion")
    print("4-Agregar eliminar artista")
    print("5-organizar playlist")
    print("6-Salir")
    ctrl=int(input("Selecciona la opcion: "))
    match ctrl:
        case 1:
            print("selecciono la opcion 1")
            x= artista(listareproduccion)
            print()
        case 2:
            print("selecciono la opcion 2")
            agregarArtista(listareproduccion)
        case 3:
            print("selecciono la opcion 3")
            agregarCancion(listareproduccion)
        case 4:
            print("selecciono la opcion 4")
            eliminarArtista(listareproduccion)
        case 5:
            ordenarLista(listareproduccion)
        case 6:
            print("saliste")
            break