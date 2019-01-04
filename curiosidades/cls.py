"""
    TIPOS DE MÉTODO 
        MÉTODO DE INSTANCIA :
            metodo comun y corriete al igual que otro lenguajes , solo puede ser accedido y se instacia la clase en la que se encuentre

        MÉTODO ESTÁTICO :
            Para crear un método estatico es necesario anteponer @staticmethod para asi indicarles a python,las caracteristicas mas comunes de un metodo estatico que al igual que java no necesita ser instaciada para poder usarse

        
        MÉTODO DE CLASE :
            @classmethod , este metodo comparte caracteristicas con el método estático , dicha caracteristica es que este emtodo puede ser llamado sin crear una instancia de la clase
            .La diferencia recae en la capacidad de acceder otros métodos y atributos de la clase.Sin embargo este tipo de metodo no tienen accesos a tributos de instacia
"""

class Auto :

    @staticmethod
    def estatico(nombre):
        return f'Hola {nombre} soy estatico y no dependo de una instacia '

print(Auto.estatico('Thom'))


class Math:
    @staticmethod
    def factorial(number):
        if number == 0:
            return 1
        else:
            return number * Math.factorial(number - 1)


factorial = Math.factorial(5)
print(factorial)

class MethodTypes:

    name = "Ragnar"

    def instanceMethod(self):
        # Creates an instance atribute through keyword self
        self.lastname = "Lothbrock"
        print(self.name)
        print(self.lastname)

    @classmethod
    def classMethod(cls):
        # Access a class atribute through keyword cls
        cls.name = "Lagertha"
        cls.g = 3
        # cls.lastname="asdasd"
        cls.sdsd = "wdsd"
        print(cls.name)
        # print(cls.lastname)
        print(cls.g)
    @staticmethod
    def staticMethod():
        print("This is a static method")

# Creates an instance of the class
m = MethodTypes()
# Calls instance method
m.instanceMethod()


MethodTypes.classMethod()
MethodTypes.staticMethod()
