def palindromo(cadena):
    cad = cadena[::-1]
    if cad.lower() == cadena.lower() :
        print("Es palindromo")
    else :
        print("No es palindromo")

while True : 
    palindromo(input('Ingrese una cadena a verificar : '))
    opcion = input("Desea continuar : ")
    if opcion=="no" :
        break