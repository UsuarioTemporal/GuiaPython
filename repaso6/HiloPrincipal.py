from Hilo1 import *
from Hilo2 import *

hilo1=Hilo1("Hilo Thom 1",1,"thom 1")
hilo2=Hilo2("Hilo Thom 2",2,"thom 2")

start = time.time()

hilo1.start()
hilo1.join()
hilo2.start()
hilo2.join()
end=time.time()

print("El tiempo transcurrido es {}".format(end-start))