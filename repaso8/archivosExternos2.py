from io import open

archivo = open("repaso8/archivo.txt","r") # PARA LEER Y ESCRIBIR SE USARÁ r+

print(archivo.read())
archivo.seek(0)
print(archivo.readlines())

