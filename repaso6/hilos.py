import threading
import time
import datetime
import logging

def consultar(id_persona):
    time.sleep(2)
    
def guardar(id_persona,data):
    time.sleep(5)
    

start=datetime.datetime.now();
t1 = threading.Thread(name="hilo_1",target=consultar,args=(1, ))
t2 = threading.Thread(name="hilo_2",target=guardar,args=(1, "Thom"))

t1.start()
t2.start()

end=datetime.datetime.now()

print("El tiempo transcurrido es {} ".format(end-start))