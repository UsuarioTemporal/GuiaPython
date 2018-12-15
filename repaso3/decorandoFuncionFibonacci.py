def memoize(func):
    cache={}
    def wrapper(*args,**kwargs):
        pass
    return wrapper

@memoize
def fib(num):
    return num