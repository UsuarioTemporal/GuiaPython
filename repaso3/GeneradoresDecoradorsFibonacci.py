#!/usr/bin/env python3

def memoize(func):
    pass

# @memoize
def fibonacci(number) :
    if number ==1 or number ==2 :
        yield number-1
    else :
        yield fibonacci(number-1)+fibonacci(number-2)

ObjetoIterable =fibonacci(5)
print(next(ObjetoIterable))