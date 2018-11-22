#  continue -- saltar a la siguiente iteracion de bucle y pasa ala siguiente iteracion
#  pass -- devolvera un null en cunato se lea

for character in "String" : 
    if character == "i" :
        continue
        # pass
    print("Letra "+character)

def contarSoloCaracteres (cadena) :
    i = 0
    for item in cadena :
        if(item==" "):
            continue
        i+=1
    return i
    

palabra = input("Ingrese una palabra : ")
print(f"La cantidad de caracteres originales de la cadena es : {contarSoloCaracteres(palabra)}")