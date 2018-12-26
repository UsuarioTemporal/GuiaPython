from threading import Thread
import time
import logging

logging.basicConfig(lebel=logging.DEBUG,format='[%(levelname)s (%(threadName)-s) %(message)s]')
class Hilo2(Thread) :
    def __init__(self,nameThread,idPersona,data):
        Thread.__init__(self,name=nameThread,target=Hilo2.run)
        # Thread.__init__(self,name=nameThread,target=__guardar,args=(self,idPersona,data))
        self.__nameThread=nameThread
        self.__idPersona=idPersona
        self.__data=data
    def run(self):
        self.__guardar(self.__idPersona,self.__data)
    
    def __guardar(self,idPersona,data):
        logging.debug("Guardando para el id "+str(idPersona)+" la data "+str(data))
        time.sleep(3)
        return 