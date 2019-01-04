import pickle

ficheroBinario = open("repaso9/listaNombre","rb") # read binary

lists = pickle.load(ficheroBinario)
print(lists)