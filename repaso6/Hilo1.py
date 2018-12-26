import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,format="[%(levelname)s] (%(threadName)-s) %(message)s")

class Hilo1(threading.Thread) : #no mames se parece a JAVA
    def __init__(self,nameThread,idPersona,data):
        self.__nameThread = nameThread
        self.__idPersona=idPersona
        self.__data=data
    def run(self):
        self.__consultar(self.__idPersona)
    
    def __consultar(self,idPersona):
        logging.debug("Consultando ")