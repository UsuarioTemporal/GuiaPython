class Operation():
    def __init__(self,number1,number2):
        self.__number1 = number1
        self.__number2 = number2
    def sumar(self):
        return int(self.__number1+self.__number2)
    def resta(self):
        return int(self.__number1-self.__number2)

if __name__ == '__main__' :
    o = Operation(5,4)
    print(o.sumar())
    print(o.resta())