import time
from threading import Thread

class MyThread(Thread):
    def run(self):
        print(f'{self.getName()} Inicio')
        time.sleep(1)
        print(f'{self.getName()} teminado')

if __name__ =='__main__' :
    for x in range(11):
        hilo = MyThread(name=f'Thread - {x}')
        hilo.start()
        time.sleep(1)