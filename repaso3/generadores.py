"""
    los generadores son estructuras que extraen informacion 
    de las funciones y que los almacenan en objetos iterables
    (que se pueden recoger)
"""

import random

def generarListaconPares(terminos) : 
    lista = []
    while terminos>0 : 
        aleatorio = random.randint(0,100)
        if aleatorio %2 ==0 :
            lista.append(aleatorio)
            terminos-=1
    
    return lista
            

numeroTerminos = int(input("Ingrese el numero de terminos : "))
print(generarListaconPares(numeroTerminos))




"""
    Los generadores son mas eficientes que las funciones tradicionales
    muy utilies con listas de valores infinitos
    bajo determinados escenarios , será muy util que un generador devuelva los
    valores de uno en uno
"""

print("Generadores")
def generarNumero(terminos) : 
    lista = []
    while terminos>0 :
        aleatorio = random.randint(0,100)
        if aleatorio %2 ==0 :
            lista.append(aleatorio)
            yield lista
            terminos-=1
    
# Debo almacenarlo n un objeto iterable
ObjetoIterable = generarNumero(10)

# for item in ObjetoIterable : 
#     print(item)



# si quiero imprimir los tres primeros elementos de mi objeto itereable

print(next(ObjetoIterable))
print(next(ObjetoIterable))
print(next(ObjetoIterable))

