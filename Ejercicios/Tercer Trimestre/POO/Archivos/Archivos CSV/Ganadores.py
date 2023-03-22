class Ganadores:
    def __init__(self,index, year, age, name, movie):
        self.__index=index
        self.__year=year
        self.__age=age
        self.__name=name
        self.__movie=movie
    def nombrePelicula(self):
        return self.__movie+' '