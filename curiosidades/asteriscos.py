# Existe dos tipos importantes al programar en python los asteriscos dobles y los asteriscos simples
# estos se utilizan en los parametros de las funciones y tambien en los argumentos de las funciones
# fuente : https://code.i-harness.com/es/q/9025
def imprime(var1,var2,var3) : 
    print(var1)
    print(var2)
    print(var3)

lista = [1,2,3,3]
# el asterisco permite recibir multiples argumentos usando una lista , tupla o diccionario
# tener cuidado con numero de elementos de mi estructura , debe concordar con el numero de 
# elementos que tiene mi funcion en el parametro
try :
    imprime(*lista)
except TypeError :
    print("funcion super llena , falta de variables")