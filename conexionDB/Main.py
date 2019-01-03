from Conexion import *

# cx = Conexion()
try:
    cx = Conexion("localhost", "root", "mysql","tienda_java")
    
except Exception as ex:
    print(ex)
finally :
    cx.cerrarConexion()