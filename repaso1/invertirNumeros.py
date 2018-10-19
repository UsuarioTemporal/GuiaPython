def invertir(numero):
    aux=0;
    numeroCambiante=numero
    while numeroCambiante!=0:
        aux=aux*10 + numeroCambiante%10
        numeroCambiante//=10
    print(aux)
    if aux == numero :
        print("El número ",numero," es capicua")
    else :
        print("El número ",numero,"no es capicua")


print("Invirtiendo numero")
numero = int(input("Ingrese el número a invertir : "))
invertir(numero)