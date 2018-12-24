def recursive_generator(lis):
    if lis:
        yield lis[0]
        yield from recursive_generator(lis[1:])


for item in recursive_generator([6,3,9,1]):
    print(item,end=' ')