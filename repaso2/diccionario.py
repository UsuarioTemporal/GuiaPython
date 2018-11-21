diccionario = {"Key":"valor",4:"cuatro","tres":3,2:1}
# print(type(diccionario))
print(diccionario)
print(diccionario.get("Key"))
print(diccionario["Key"])
print(diccionario.keys())
print(diccionario.values())

diccionario["clave"]="V"
del diccionario[4]
print(diccionario)
diccionario["clave"]="nuevo valor"
print(diccionario)

# Prueba
print("\nJugando con las estructuras Lista ")
lista = ["primero","segundo","tercero",5,("primeroTupla",5),[1,7]]

tupla = (lista,15,47)

for item in lista : 
    # print(type(item))
    print(item)

print("\nJugando con estructuras de datos tuplas")
for item in tupla : 
    # print(type(item))
    print(item)


print("\nJugando con estructuras de datos diccionarios : ")
miDiccionario ={1:lista,2:tupla,lista[0]:{14:5,4:diccionario}}

for key in miDiccionario.keys() :
    print(miDiccionario[key],end="\n")