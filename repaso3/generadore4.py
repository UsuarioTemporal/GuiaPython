class PrimerosN(object) : 
    def __init__(self,terminos):
        self.terminos =terminos
        self.numero , self.listaNumeros = 0,[]

    def __iter__(self): #funcion iterable
        return self

    #retornara el sigueinte 
    def __next__(self) : 
        return self.next()
    def next(self) : 
        if self.numero < self.terminos :
            pass