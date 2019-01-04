"""
    Consiste en guardar en un fichero externo una coleccion o un objeto , pero lo mas importante es que esto se guardara en un archivo codificado , encriptado (codigo binario)
"""
import pickle
listaNombres = ["Pedro","Ana","Maria","Isabel"]
ficheroBinario = open("repaso9/listaNombre","wb")
pickle.dump(listaNombres,ficheroBinario)
ficheroBinario.close()
del (ficheroBinario)