from Aprendiz import *                                          #Se importa la clase Aprendiz con sus metodos
from Curso import *                                             #Se importa la clase Curso a este archivo

nombre=input('ingrese nombre del aprendiz')                     #Se crea una variable para ingresar el nombre del aprendiz
documento=int(input('ingrese documento del aprendiz'))          #Se crea otra variable para ingresar el documento del aprendiz
ficha=input('ingrese ficha del aprendiz')                       #Se crea otra variable para ingresar la ficha del aprendiz

ap=Aprendiz(ficha,nombre,documento)                             #Se crea un objeto para aprendiz, el cual va a tener como atributos los input puestos anteriormente

nombreCurso=input('ingrese nombre del curso')                   #Se crea una variable para ingresar el nombre del curso
horas=int(input('ingrese intensidad horaria del curso'))        #Se crea otra variable de input y de numeros enteros para ingresar las horas del curso
c1=Curso(nombreCurso,horas)                                     #Se crea un objeto para curso el cual va a tener como atributos los 2 input crados previamente.
ap.agregarCurso(c1)                                             #Se indica que en la clase aprendiz, se va a agregar el curso anteriormente mencionado.

with open('Archivos/aprendices.txt','a') as flujo:              
    flujo.write(ap.getFicha()+','+ap.getNombre()+','+str(ap.getDocumento())+'\n')

#Se crea un with open para crear un flujo en el archivo puesto en la ruta. Se crea el metodo para escribir en el archivo
#Se colocan los metodos de getter para obtener los datos e ir agregandolos, se utiliza el operador aritmetico "+" para
#juntar todas las cadenas y se pongan en una misma linea. Se coloca un str para que los datos sean una cadena legible
#y se separa por comas. Al final se agrega un salto de linea para cuando se agreguen mas datos, se visualicen en otra linea
#de codigo. 