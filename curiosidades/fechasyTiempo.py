import time
print('Tiempo sin formato')
print(time.time())
print('\nTiempo con formato,24h')
print(time.strftime('%H : %M : %S')) # dandole formato

print('\nTiempo con formato,12h')
print(time.strftime('%I : %M : %S'))

print('\nFechas')
print(time.strftime('%d / %m / %y'))