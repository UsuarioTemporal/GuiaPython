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
    listaDePersonas=[]
    def __init__(self):
        self.personas=[]
        
    def addPersonas(self,p):
        self.personas.append(p)

    def guardarPermanente(self):
        listaDePersonas=open("repaso10/ficheroExterno","wb")
        pickle.dump(self.personas,listaDePersonas)
        listaDePersonas.close()
        del listaDePersonas

    @classmethod
    def mostrarPermanente(cls):
        cls.listaDePersonas=open("repaso10/ficheroExterno","rb")
        cls.lista= pickle.load(cls.listaDePersonas)
        cls.listaDePersonas.close()
        del cls.listaDePersonas
        

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
lista.guardarPermanente()

ListaPersonas.mostrarPermanente()