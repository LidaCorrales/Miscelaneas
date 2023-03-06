class Aprendiz:                                 #Se crea una clase llamada Aprendiz
    def __init__(self,nombre):                  #Se agrega un constructor con los parametros self y nombre
        self.__nombre=nombre                    #Se inicializa con el self al atributo llamado nombre.
        self.__cursos=[]                        #Se crea el atributo de una lista que almacene los cursos
    def agregarCurso(self,nombreCurso):         #Se crea un metodo para agregar curso con el parametrro del nombreCurso
        self.__cursos.append(nombreCurso)       #Se utiliza la funcion append para agregar el nombre del curso a la lista vacia
    def verCursos(self):                        #Se crea un metodo para ver los cursos con solo el parametro self
        return self.__cursos                    #Se retorna el atributo de cursos

class Curso:                                    #Se crea una clase llamada Curso
    def __init__(self,nombreCurso):             #Se agrega un constructor con el parametro self y nombreCurso
        self.__nombreCurso=nombreCurso          #Se incializa con el self el parametro llamado nombreCurso.

    def getNombreCurso(self):                   #Se crea un getter para el nombreCurso, esto para poder visualizarlo.
        return self.__nombreCurso               #Se retorna el nombreCurso
    
ob=Aprendiz('Miguel')                           #Se crea el objeto y se llama a la clase aprendiz con su parametro correspondiente.
c1=Curso('Python Basico')                       #Se crea una variable para el objeto de Curso, este primer objeto consiste en el primer curso que se agrega.
c2=Curso('Python Intermedio')                   #Se crea otra variable para agregar un segundo curso
c3=Curso('Java Basico')                         #Se crea otra variable para agregar el tercer curso

ob.agregarCurso(c1)                             #Se llama al objeto junto con el metodo de agregarCurso para que añada el primer curso
ob.agregarCurso(c2)                             #Se llama otra vez al objeto con el metodo para añadir el segundo curso
ob.agregarCurso(c3)                             #Se llama por ultimo al objeto con el metodo para añadir el tercer curso

for curso in ob.verCursos():                    #Se crea un for para iterar cada objeto que se almacena en verCursos
    print(curso.getNombreCurso())               #Se imprime el metodo getter para mostrar todos los objetos que se encuentran guardados.

del ob                                          #Se borra el objeto
#print(ob)
print('.....',c1.getNombreCurso())              #Se imprime con una cadena y el getter para diferenciar el curso, una vez borrado el objeto.