class Objeto() : 
    pass
class OtroObjeto :
    pass
print("Objetos : ")
print(type(OtroObjeto))
print(type(Objeto))

obejto = Objeto() #instanciando una clase 
clase = Objeto # asignando clase

print("Objeto de la clase propia creada")
print(type(obejto))
print("Igualando clases")
print(type(clase))


# Usando la clase OtroObjeto
otroObjeto = OtroObjeto() #instanciando otro objeto
claseoOtroObejto = OtroObjeto
print(type(otroObjeto))
print(type(claseoOtroObejto))