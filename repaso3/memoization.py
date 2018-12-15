#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

def fib(num):
    if num ==1 or num==2 :  
        return num-1
    else :
        return fib(num-1) + fib(num-2)
start = time.time()
print(fib(20))
end= time.time()
print("El tiempo en segundos de ejecucion es {} segundos".format(end-start))