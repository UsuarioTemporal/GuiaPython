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
            cur,self.numero = self.numero+1,self.numero+1
            return cur
        else :
            raise StopIteration()


# suma = sum(PrimerosN(10))
# print (suma)
for itemClass in PrimerosN(10) :
    print(itemClass)

