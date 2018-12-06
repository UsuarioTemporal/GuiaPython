lista = [2 * num for num in range(10)] 
Objeto = (2 * num 
            for num in range(10))

#  Quizá en este ejemplo no veas la diferencia 
# print('Lista')
# for item in lista : 
#     print(item)

# print('\nObjeto')
# for item in Objeto : 
#     print(item)

# Aquí esta lo mas bonito , TEORIA , todo es teoria
print(type(lista))
print(type(Objeto))