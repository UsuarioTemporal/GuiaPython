import math 

def calculaRaiz(numero1) : 
    if numero1 < 0 : 
        raise BaseException("No puede ser negativo")
    else :
        return math.sqrt(numero1)
try :
    print(calculaRaiz(-1))
except BaseException as Err :
    print("Capturando exception de tipo ",Err.__class__)