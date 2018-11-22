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