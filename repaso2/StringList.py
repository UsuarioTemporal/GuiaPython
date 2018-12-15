string = '123456'
print(string[0])
print(len(string))
print(string[-1])
print(string[: -5])
print(string[-5:])
print(string[-6])
print(string[-1::-6]) # inicio : final : saltos
print(string[::-1])
print(string[-6::])
print(string[0:7:2])

# convertir string a minusculas
#string=string.lower()
#convertir string a mayuscular
#string=string.upper()
#result=string.find('c')
#result = string.count('c')
#newString = string.replace('c',''x')
#newString=string.split(' ') esto separa la cadenas en blokes respecto a los espacios
# y esto retornara una lista

# creamos un archivo txt (texto.txt) esta en esta misma carpeta
archivo = open("repaso2/texto.txt","r")
texto =archivo.read().split(" ")
print(texto)
