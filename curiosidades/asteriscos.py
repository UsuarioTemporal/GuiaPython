# Existe dos tipos importantes al programar en python los asteriscos dobles y los asteriscos simples
# estos se utilizan en los parametros de las funciones y tambien en los argumentos de las funciones
# fuente : https://code.i-harness.com/es/q/9025
def imprime(var1,var2,var3) : 
	print(var1)
	print(var2)
	print(var3)

lista = [1,2,3]
# los asteriscos permiten recibir multiples argumentos usando una lista , tupla o diccionario
# tener cuidado con numero de elementos de mi estructura , debe concordar con el numero de 
# elementos que tiene mi funcion en el parametro
try :
	imprime(*lista) # los asteriscos simples se usaran para listas y tuplas
except TypeError :
	print("funcion super llena , falta de variables")

# los asteriscos dobles se usaran para los diccionarios pero si queremos decidir cuantos parametros le añadiremos
# el nombre de las llaves debe ser igual al nombre de los parametros
def funcion(var1,var2,var3):
	print(var1)
	print(var2)
	print(var3)

diccionario = {'var1':'item1','var2':'item2','var3':'item3'}
funcion(**diccionario)

#imagenemos que no sabemos el numero de elementos de parametros
tupla=(1,5,5)
def datos(*args):
	# print(args)
	print(len(args[0]))

datos(lista)

def datosDiccionarios(**kwargs):
	print(kwargs)
	# print(type(kwargs))

datosDiccionarios(**diccionario)

def funcionCompleta(*args,**kwargs):
	# print(args)
	# print(kwargs)
    print(args)
    print(kwargs)


print("Primera opcion")
funcionCompleta(lista,**diccionario) # la lista se alamacena en una tupla
print("\nSegunda opcion")
funcionCompleta(*lista,**diccionario) # la lista se convierte en una tupla
print("\nTercera opcion")
funcionCompleta(*lista,*diccionario) # las llaves de los diccionarios se agregaran a la tupla
print("\nCuarta opcion")
funcionCompleta(lista,*diccionario) # las llaves de los diccionarios se agregaran a la tupla
funcionCompleta(lista,diccionario) # el diccionario se agregara a la tupla