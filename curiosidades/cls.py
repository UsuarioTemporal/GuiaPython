"""
    TIPOS DE MÉTODO 
        MÉTODO DE INSTANCIA :

        MÉTODO ESTÁTICO :
            Para crear un método estatico es necesario anteponer @staticmethod para asi indicarles a python,las caracteristicas mas comunes de un metodo estatico que al igual que java no necesita ser instaciada para poder usarse

        
        MÉTODO DE CLASE :
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

