from Conexion import *

# cx = Conexion()
try:
    cx = Conexion("localhost", "root", "mysql","tienda_java")
    cx.commit()
except Exception as ex:
    print(ex)
finally :
    cx.cerrarConexion()
