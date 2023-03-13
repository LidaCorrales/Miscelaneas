from Aprendiz import *                          #Se importa la clase Aprendiz
from Curso import *                             #Se importa la clase Curso

ap=Aprendiz('2560664A','Diego Suarez',123456)   #Se crea un objeto para la clase Aprendiz, en los parametros se agrega los datos que contendra.
c1=Curso('Python Intermedio',200)               #Se crea una objeto para la clase Curso, se agregan a los parametros los datos que contendran.
c2=Curso('Python Avanzado',200)                 #Se crea un segundo objeto para Curso, agregando diferentes datos a este.
#print(c1.getNombre())
ap.agregarCurso(c1)                             #Se llama al atributo agregarCurso para que añada el primer objeto a la clase Curso
ap.agregarCurso(c2)                             #Se hace lo mismo para agregar otro objeto

for curso in ap.getCursos():                    #Se agrega un for para recorrer todos los objetos contenidos en la clase Cursos
    print(curso.getNombre())                    #Se imprime el atributo de nombres para mostrar todos los objetos contenidos en este.