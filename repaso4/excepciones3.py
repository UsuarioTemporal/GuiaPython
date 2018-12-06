import math 

def calculaRaiz(numero1) : 
    if numero1 < 0 : 
        raise BaseException("No puede ser negativo")
    else :
        return math.sqrt(numero1)

print(calculaRaiz(-1))