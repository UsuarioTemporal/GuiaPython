from io import open

archivo = open("repaso8/archivo.txt","r")

print(archivo.read())
archivo.seek(0)
print(archivo.readlines())