import time 
def memoize(func):
    cache={}
    def wrapper(*args,**kwargs):
        if args not in cache :
            cache[args]=func(*args,**kwargs)
        return cache[args]
    return wrapper

@memoize
def fib(num):
    if num ==1 or num==2 :  
        return num-1
    return fib(num-1) + fib(num-2)

start =time.time()
print(fib(1000))
end=time.time()
print("El tiempo en segundos de ejecucion es {} segundos".format(end-start))



"""





"""
