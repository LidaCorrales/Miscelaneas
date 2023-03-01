class Persona:                              #Se genera un nuevo tipo de dato llamado "Persona", que se crea en una clase
    def __init__(self,nombre,doc):          #Se crea un metodo dentro de la clase, llamado constructor. La cual tiene de parametro self para indicar que se encuentra en la funcion y el segundo parametro nombre.
        self.__nombre=nombre                    #Se inicializa con el self al atributo llamado nombre que se le puso al contenido, en este caso llamado nombre.
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

ob=Persona('Maria', 18734)
print(ob.getNombre())
ob.setNombre('Ana')
print(ob.getNombre())
ob.setDoc(76543)
print(ob.getDoc())
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