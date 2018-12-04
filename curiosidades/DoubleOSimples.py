import this
# He tenido problemas con el interprete al usar comillas dobles y aveces 
# problemas al usar problemas simples 

#fuentes : https://recursospython.com/guias-y-manuales/comillas-dobles-o-simples/
#          http://recursospython.com/guias-y-manuales/zen-de-python-tim-peters/
#          http://www.recursospython.com/pep8es.pdf


# Según la documentacion , para aquellos modulos que expresan ua funcion deben ser declarados por 
# comillas triples

def suma() : 
    a,b=1,2
    """Esto retornara la los dos valores como tupla"""
    return a,b

"""Sumando los valores de la tupla"""
print(sum(suma()))
