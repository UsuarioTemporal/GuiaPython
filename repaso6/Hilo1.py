from threading import Thread
import time
import logging

logging.basicConfig(level=logging.DEBUG,format="[%(levelname)s] (%(threadName)-s) %(message)s")

class Hilo1(Thread) : #no mames se parece a JAVA
    def __init__(self,nameThread,idPersona,data):
        Thread.__init__(self,name=nameThread,target=Hilo1.run)
        self.__nameThread = nameThread
        self.__idPersona=idPersona
        self.__data=data
        # super().__init__
    def run(self): # al igual que JAVA esto servira para que comience el hilo 
        self.__consultar(self.__idPersona)
        
    
    def __consultar(self,idPersona):
        logging.debug("Consultando el id de persona "+str(idPersona))
        time.sleep(2)
        return 