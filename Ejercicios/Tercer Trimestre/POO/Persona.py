class Persona:                              #Se genera un nuevo tipo de dato llamado "Persona", que se crea en una clase
    def __init__(self,nombre,doc):          #Se crea un metodo dentro de la clase, llamado constructor. La cual tiene de parametro self para indicar que se encuentra en la funcion y el segundo parametro nombre.
        self.__nombre=nombre                #Se inicializa con el self al atributo llamado nombre que se le puso al parametro, llamado nombre.
        self.__doc=doc
        #print('Constructor Activado')        

    def getNombre(self):                    #Se crea un getter con el parametro self. Self significa que el parametro esta dentro de persona.
        return self.__nombre                #Se retorna el atributo nombre como metodo de self. Se instancia.

    def setNombre(self,nombre):             #Se crea un setter con el parametro self y nombre.
        self.__nombre=nombre                #Inicializar un dato unico que contiene la palabra reservada self y el nombre como parametro.

    def getDoc(self):
        return self.__doc
    
    def setDoc(self,doc):
        self.__doc=doc

ob=Persona('Maria', 18734)                  #Se crea un objeto para asignarle variables de instancia.
print(ob.getNombre())                       #Se imprime el objeto con el metodo del getter de nombre.
ob.setNombre('Ana')                         #se llama al objeto con el metodo de set nombre y se le asigna un valor de cadena.
print(ob.getNombre())                       #Se imprime el getter de nombre con el valor asignado
ob.setDoc(76543)                            #Se llama al objeto con el metodo de get documento con una variable de int
print(ob.getDoc())                          #Se imprime el getter de documento con el valor asignado.
#print(type(ob))

class Aprendiz(Persona):
    def __init__(self,nombre,ficha,doc):
        Persona.__init__(self,nombre,doc)
        self.__ficha=ficha

    def getFicha(self):
        return self.__ficha
    
    def getAll(self):
        print(Persona.getNombre(self), Persona.getDoc(self), self.__ficha, end=' ')

app=Aprendiz('Pedro',12345,1837727)
app.getAll()