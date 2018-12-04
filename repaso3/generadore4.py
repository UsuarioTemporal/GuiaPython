class PrimerosN(Object) : 
    def __init__(self,terminos):
        self.terminos =terminos
        self.numero , self.listaNumeros = 0,[]

    def __iter__(self): #funcion iterable
        return self

    