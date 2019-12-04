class User:
    __slots__ = ['name','age']
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    user1 = User('ThomMaurick',21)
    print(user1.name)
    print(user1.age)