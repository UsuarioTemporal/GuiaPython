from abc import ABCMeta , abstractmethod

#interface
class Figura(object):
    __metaclass__=ABCMeta

    @abstractmethod
    def area(self):pass
        
    @abstractmethod
    def perimetro(self) :pass

class Rectangulo(Figura):
    def __init__(self,ancho,altura):
        self.__ancho=ancho
        self.__altura=altura
        super(Rectangulo,self).__init__()

    def area(self):
        return self.__altura*self.__ancho
    def perimetro(self):
        return self.__altura*2 + self.__ancho*2
cuadrado=Rectangulo(45,4)