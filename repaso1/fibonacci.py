def fibonacci(numeroTerminos):
    suma = 0 
    pre = 0
    post = 1
    for i in range(numeroTerminos):
        print(pre)
        suma=pre+post
        pre=post
        post=suma


numeroTerminos = int(input("Ingrese el número de terminos"))
fibonacci(numeroTerminos)
