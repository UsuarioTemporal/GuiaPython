import pickle

class Persona :
    def __init__(self, nombre,genero,edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Persona creada en ",self)
    def __str__(self):
        return f"{self.nombre} {self.genero} {self.edad}"

class ListaPersonas :
    def __init__(self):
        self.listaDePersonas = open("repaso10/ficheroExterno","ab+")
        self.listaDePersonas.seek(0)
        self.personas=[]
        try:
            self.personas=pickle.load(self.listaDePersonas)
        except Exception as ex:
            pass
        finally :
            self.listaDePersonas.close()
            del (self.listaDePersonas)
    def addPersonas(self,p):
        self.personas.append(p)
    
    def showPersonas(self):
        return [p.__str__() for p in self.personas]

p1 = Persona("Thom","Masculino",20)
p2 = Persona("Carlos","Masculino",22)
p3 = Persona("Andres","Masculino",24)

lista = ListaPersonas()
lista.addPersonas(p1)
lista.addPersonas(p2)
lista.addPersonas(p3)

print(lista.showPersonas())