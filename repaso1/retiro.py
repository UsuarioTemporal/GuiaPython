class Cajero :

    def __init__(self,password=''):
        self.password=password
        self.dollarClass = [i  for i in range(0,105,5) ]
        self.dollarClass[0]=1
    def check(self):
        return self.password == '12345'
    def distribute (self,dollar):
        for dollar in self.dollarClass :
            pass

cajero1 = Cajero('12345')
if cajero1.check(): 
    print(cajero1.dollarClass)
else :
    print('No ingreso')
