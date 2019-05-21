#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

def fib(num): #funcion ineficiente
    if num ==1 or num==2 :  
        return num-1
    else :
        return fib(num-1) + fib(num-2)

#funcion eficiente
cache = {}
def fibo(num):
    if num ==1 or num==2 :  
        return num-1
    if num not in cache :
        cache[num]= fibo(num-1)+fibo(num-2)
    return cache[num]
start = time.time()
# print(fib(34)) #ineficiente
print(fibo(999)) #eficiente
end= time.time()
print("El tiempo en segundos de ejecucion es {} segundos".format(end-start))
