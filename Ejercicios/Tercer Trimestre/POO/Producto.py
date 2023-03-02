class Producto:
    counter = 0
    def __init__(self, nombre,precio):
        self.__nombre=nombre
        self.__precio=precio
        Producto.counter +=1

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre=nombre

    def getPrecio(self):
        return self.__precio
    
    def setPrecio(self, precio):
        self.__precio=precio

    def IncludIva(self):
        iva=self.__precio*0.19
        return iva

    def getAll(self):
        print(Producto.getNombre(self), Producto.getPrecio(self), Producto.IncludIva(self), end="\t")


ob=Producto('Maria',1287)
ob2= Producto('Luisa', 1323)
ob3=Producto('Juan', 162)
print(Producto.counter)
ob.getAll()
ob2.getAll()
ob3.getAll()