from conexionDB import Conexion

try:
    cx = Conexion.Conexion("localhost", "root", "mysql","tienda_java")
    sql = "CREATE TABLE IF NOT EXISTS producto(id_producto INT PRIMARY KEY AUTO_INCREMENT,nombre_producto VARCHAR(20) NOT NULL,precio_producto DECIMAL(10,2) NOT NULL)"
    insert = ""
    update = ""
    delete =""
    show =""
    # cx.ejecutarQuery(sql)
    cx.commit()
except Exception as ex:
    print(ex.__dict__)
finally :
    cx.cerrarConexion()
variosProductos=[
    ("Papa",2.5),
    ("Pan",1.5),
    ("Arroz",3.5)
]
# miCursor.executemany("INSERT INTO producto(nombre_producto,precio_producto) VALUES(?,?)",variosProductos)
