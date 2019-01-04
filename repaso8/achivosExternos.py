from io import open # esto servira para poder abrir un archivo

archivo = open("repaso8/archivo.txt","r") #w , a , r

frase = "Que pex\n"
# archivo.write(frase)
print(archivo.read())
archivo.close()