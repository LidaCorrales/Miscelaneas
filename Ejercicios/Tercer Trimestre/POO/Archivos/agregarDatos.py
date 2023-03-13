from Aprendiz import *                                      #Se importa la clase Aprendiz a este archivo
from Curso import *                                         #Se importa la clase Cursos a este archivo

# nombre=input('ingrese nombre del aprendiz')
# documento=int(input('ingrese documento del aprendiz'))
# ficha=input('ingrese ficha del aprendiz')

# ap=Aprendiz(ficha,nombre,documento)

# nombreCurso=input('ingrese nombre del curso')
# horas=int(input('ingrese intensidad horaria del curso'))
# c1=Curso(nombreCurso,horas)
# ap.agregarCurso(c1)

# with open('herencia/aprendices.txt','a') as flujo:    
#     flujo.write(ap.getFicha()+','+ap.getNombre()+','+str(ap.getDocumento())+'\n')

with open('Archivos/aprendices.txt','r') as flujo:          #Se agrega el with open as flujo para escribir en el archivo contenido por la ruta, ademas de la accion escrita 'r'.
    datos=flujo.read()                                      #Se crea un variable para que lea lo que se encuentra en el archivo.
    print(datos)                                            #Se imprimen para mostrar los datos que contiene el archivo de la ruta.
    #flujo.write('2560664,maria,123')
aprendices=[]                                               #Se crea una lista vacia llamada aprendices
with open('herencia/aprendices.txt','r') as flujo:          #Se agrega el with open as flujo con la misma ruta.
    for linea in flujo:                                     #Se agrega un for para recorrer cada dato de flujo, es decir, del archivo.
        #print(linea)
        aprendices.append(linea.rsplit())                   #A la lista se le van agregando con el append, todos los datos dividiendolos en subcadenas.

datosxlinea=[]                                              #Se crea una lista vacia llamada datosxlinea.
for aprendiz in aprendices:                                 #Se agrega un for para recorrer todas las listas de aprendices.
    datosxlinea.append(aprendiz[0].split(','))              #A la lista se le va agregando con el append, el primer dato de todas las listas de aprendiz, separados por una coma (',').

#print(ob.getNombre())

print(datosxlinea)                                          #Se imprime la lista creada. Que consiste en los primeros datos obtenidos por cada lista. 

listaDeObjetos=[]                                           #Se crea una lista llamada listaDeObjetos
for apr in datosxlinea:                                     #Se crea un for para recorrer todos los datos de la lista 'datosxlinea'
     f=apr[0]                                               #Se crea una variable para hayar el primer dato contenido en la lista
     n=apr[1]                                               #Se crea otra variable para hayar el segundo dato contenido en la lista
     d=apr[2]                                               #Se crea otra variable para hayar el tercer dato contenido en la lista.
     ob=Aprendiz(f,n,d)                                     #Se crea un objeto para la clase aprendiz, esto para que agregue los datos obtenidos como atributos.
     print(ob)                                              #Se imprime el objeto
     listaDeObjetos.append(ob)                              #A la lista se le agrega un append, para que vaya agregando los datos obtenidos en el objeto.

for xx in listaDeObjetos:                                   #Se crea un for para recorrer la lista llamada listaDeObjetos
    print(xx.getNombre())                                   #Se imprime el primer atributo añadido mostrandolo con el getter
    print(xx.getDocumento())                                #Se imprime el segundo atributo agregado mostrandolo con el getter
    print(xx.getFicha())                                    #Se imprime el tercer atributo añadido mostrandolo con un getter.