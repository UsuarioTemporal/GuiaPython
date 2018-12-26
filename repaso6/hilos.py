import threading
import time
import datetime
import logging
"""
    Por defecto python al igual que java tiene un hilo implicito que es el encargado de la ejecución , entonces
    el total es de hilos son 3 , entonces si queremos que ele hilo que ejcute se sincronize con los demas para los demas cumplan su funcion y luego al terminar cada uno , termine e hilo del main
"""


""" 
    testing python
"""
logging.basicConfig(level=logging.INFO,format='[%(levelname)s] (%(threadName)-s) %(message)s')
# logging.INFO 
# logging.WARN

def consultar(id_persona):
    logging.info("CONSULTANDO PARA EL ID "+str(id_persona))
    time.sleep(2)
    return 
def guardar(id_persona,data):
    logging.info("CONSULTANDO PARA EL ID "+str(id_persona)+" data "+str(data))
    time.sleep(3)
    return 

start=time.time()
t1 = threading.Thread(name="hilo_1",target=consultar,args=(1, ))
t2 = threading.Thread(name="hilo_2",target=guardar,args=(1, "Thom"))

t1.start() #comenzando el hilo 1 
t1.join()
t2.start() #comenzando el hilo 2


# sincronizando hilos

t2.join()


end=time.time()

print("El tiempo transcurrido es {} ".format(end-start))