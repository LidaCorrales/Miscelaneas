from datetime import datetime

class Pedido:
    def __init__(self,identi,titulo,codigo):
        self.__identi=identi
        self.__titulo=titulo
        self.__codigo=codigo

    def getIdenti(self):
        return self.__identi
    def setIdenti(self, identi):
        self.__identi=identi

    def getTitulo(self):
        return self.__titulo
    def setTitulo(self, titulo):
        self.__titulo=titulo

    def getCodigo(self):
        return self.__codigo
    def setCodigo(self, codigo):
        self.__codigo=codigo

    def Reservar(self,identi,fecha):
        self.fecha=fecha
        fecha=Lector(identi)
        self.fecha.datetime.now(fecha)
    def Entregar(self):
        fecha_ingreso=self.datetime.now(fecha_ingreso)
        return fecha_ingreso

    def Bibliotecario(self,identi):
        self.__identi=identi

class Lector:
    def __init__(self,identi,nombre,direccion,telefono):
        self.__identi=identi
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono

    def getIdenti(self):
        return self.__identi
    def setIdenti(self, identi):
        self.__identi=identi

    def getNombre(self):
        return self.__nombre
    def setIdenti(self, nombre):
        self.__nombre=nombre

    def getDireccion(self):
        return self.__identi
    def setDireccion(self, direccion):
        self.__direccion=direccion

    def getTelefono(self):
        return self.__telefono
    def setTelefono(self, telefono):
        self.__telefono=telefono

    def Estudiante(self,identi):
        self.__identi=identi
        pedir=Pedido()

    def Docente(self,identi):
        self.__identi=identi

class Material(Pedido):
    def __init__(self,titulo,tipo,autor,editorial):
        self.__titulo=titulo
        self.__tipo=tipo
        self.__autor=autor
        self.__editorial=editorial

    def getTitulo(self):
        return self.__titulo
    def setTitulo(self, titulo):
        self.__titulo=titulo

    def getTipo(self):
        return self.__tipo
    def setTipo(self, tipo):
        self.__tipo=tipo

    def getAutor(self):
        return self.__autor
    def setAutor(self, autor):
        self.__autor=autor

    def getEditorial(self):
        return self.__editorial
    def setEditorial(self, editorial):
        self.__editorial=editorial

    def Libro(self):
        return self.Libro
    
    def Revista(self):
        return self.Revista
    
    ob=Pedido(12345, "Nombre Libro", 67890)
    ob.setIdenti(12345)
    ob.setTitulo("Nombre Libro")
    ob.setCodigo(12213)
    print(ob.getTitulo())
    print(ob.getIdenti())
    print(ob.getCodigo())