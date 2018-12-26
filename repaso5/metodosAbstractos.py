from abc import ABCMeta , abstractmethod

#interface
class Figura(metaclass=ABCMeta):

    @abstractmethod
    def area(self):pass
        
    @abstractmethod
    def perimetro(self) :pass

class Rectangulo(Figura):
    def __init__(self,ancho,altura):
        self.__ancho=ancho
        self.__altura=altura
        super().__init__()

    def area(self):
        return self.__altura*self.__ancho
    def perimetro(self):
        return self.__altura*2 + self.__ancho*2
cuadrado=Rectangulo(45,4)

print("El area es {}".format(cuadrado.area()))

# pelota = Figura()