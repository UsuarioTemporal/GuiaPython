"""
    En conclusión los generadores son funciones que permitirán obtener los resultados  poco a poco 
    Es decir, cada vez que llamemos a la función nos darán un nuevo resultado. Como por ejem 
    una función para generar todos lo números pares que cada vez que la llamemos nos devulva el siguiente 
    número par
"""

""" 
    Los generadores valga la redundancia ,sirven para generar datos en tiempo de ejecución .
    Además también podemos acelerar búsquedas y crear bucles mas rápidos .  

"""
# Referencias https://wiki.python.org/moin/Generators


# los generadores nos devolveran items de uno en uno en los cuales nosotros los programadores
# tendremos que iterar
listaNumeros = [1,2,3,4,5]
listaString = ['h','o','l','a']
lista = [letra * numero 
                    for letra in listaString 
                        for numero in listaNumeros 
                            if numero> 0]

ObjetoGenerador = (letra * numero 
                    for letra in listaString 
                        for numero in listaNumeros 
                            if numero> 0)
print(lista)
print(next(ObjetoGenerador))
print(next(ObjetoGenerador))
print(next(ObjetoGenerador))