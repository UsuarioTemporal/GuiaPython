#!/usr/bin/env python3

# fibonacci generador sin recursion
def fibonacci() :
    pre,post=0,1
    while True : 
        yield pre
        pre,post=post,pre+post

count = 0 # cantidad 
terminos = 5
for item in fibonacci() :
    print(item,end=" ")
    count+=1
    if count == terminos :
        break;


# forma mas simplificada

def fibo(num) :
    pre,post,count=0,1,0
    while True :
        if  count==num : return 
        yield pre
        pre,post=post,pre+post
        count+=1
print("\n")
for item in fibo(5) :
    print(item,end=" ")

# método super simplificado
def fibona(pre = 0 ,post = 1) :
    while True :
        yield pre
        pre,post = post,pre+post

Object = fibona()
lista = [next(Object) for item in range(5)]
print("\n")
print(lista)
