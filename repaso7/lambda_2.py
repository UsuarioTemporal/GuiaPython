def first(a):
    def second(b):
        return a+b
    return second

print(first(1)(2))

def _first(a):
    return lambda b:a+b
print(_first(1)(2))
