# Existe dos tipos importantes al programar en python los asteriscos dobles y los asteriscos simples
# estos se utilizan en los parametros de las funciones y tambien en los argumentos de las funciones

def imprime(var1,var2,var3) : 
    print(var1)
    print(var2)
    print(var3)

lista = [1,2,3]
# el asterisco permite recibir multiples argumentos usando una lista , tupla o diccionario

imprime(*lista)