def fibonacci(numeroTerminos):
    suma = 0 
    pre = 0
    post = 1
    for i in range(numeroTerminos):
        print(pre,end=" ")
        suma=pre+post
        pre=post
        post=suma

def f(numeroTerminos):
        pre,post=0,1
        while(pre<numeroTerminos):
                print(pre,end=" ")
                pre,post=post,pre+post

numeroTerminos = int(input("Ingrese el número de terminos"))
# fibonacci(numeroTerminos)
f(numeroTerminos)
