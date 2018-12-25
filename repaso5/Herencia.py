class Animal() :
    def __init__(self,nombre):
        self.__nombre=nombre
    @property
    def nombre(self ):
        return self.__nombre
    @nombre.setter
    def nombre(self,value) :
        self.__nombre=value
    def values(self):
        print(self.__nombre)
class Persona(Animal) :
    def __init__(self,nombre,dni):
        super().__init__(nombre)
        self.__dni=dni
    def values(self):
        super().values()
        print(self.__dni)
# como usar correctamente los métodos getters y setters en python
carlos=Persona('Carlos','123456')
carlos.values()
class Email():
    def __init__(self,password):
        self.__password=password
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,value):
        self.__password=value

thom =Email('112')
# thom.getPassword='15'
thom.password='45'
print(thom.password)
thom.__password='58'
print(thom.__dict__)
print(thom.password)