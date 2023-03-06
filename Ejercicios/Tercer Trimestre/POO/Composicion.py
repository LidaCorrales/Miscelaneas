class Curso:                                    #Se crea una clase llamada Curso
    def __init__(self,titulo):                  #Se agrega un constructor con los parametros self y titulo
        self.__titulo=titulo                    #Se inicializa con el self al atributo llamado titulo.

    def getTitulo(self):                        #Se crea un getter con el parametro self
        return self.__titulo                    #Se retorna el objeto titulo, para su visualizacion. 

class Aprendiz:                                 #Se crea una clase llamada Aprendiz
    def __init__(self,nombre):                  #Se agrega un constructor con los parametros self y nombre
        self.__nombre=nombre                    #Se inicializa con el self al atributo llamado nombre.
        self.__cursos=[]                        #Se crea el atributo de una lista que almacene los cursos

    def agregarCurso(self,nombreCursito):       #Se crea un metodo para agregar un curso, con los parametros self y nombreCursito.
        cursito=Curso(nombreCursito)            #Se crea la variable cursito para que por medio de la clase Curso, se almacene el objeto de nombreCursito, es decir, se añada el nombre de los cursos.
        self.__cursos.append(cursito)           #Se agrega con append a la variable cursito para añadir los cursos.

    def getCursos(self):                        #se crea un getter con el parametro self.
        return self.__cursos                    #Se retorna curso para mostrar sus objetos.
    
ap=Aprendiz('Sofia')                            #Se crea un objeto llamado ap para la clase Aprendiz y se coloca su parametro correspondiente. 
ap.agregarCurso('Python Basico')                #Se llama al objeto para agregar un curso y su nombre correspondiente. 
ap.agregarCurso('Python Intermedio')            #Se llama al objeto para agregar otro nuevo curso.

for c in ap.getCursos():                        #Se crea un for para iterar todos los objetos de getCursos
    print(c.getTitulo())                        #Se imprime el getTitulo para que muestre todos los cursos que se han añadido.

del ap                                          #Al borrar el objeto, no se almacenaria ningun curso, ya que, el objeto es el responsable de crear los cursos y añadirlos. Por lo cual se utiliza objetos dentro de otros objetos.