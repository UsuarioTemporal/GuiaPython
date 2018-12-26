import threading
import time
import datetime
import logging
"""
    Por defecto python al igual que java tiene un hilo implicito que es el encargado de la ejecución , entonces
    el total es de hilos son 3 , entonces si queremos que ele hilo que ejcute se sincronize con los demas para los demas cumplan su funcion y luego al terminar cada uno , termine e hilo del main
"""
def consultar(id_persona):
    time.sleep(2)
    
def guardar(id_persona,data):
    time.sleep(5)


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