import pymysql

class Conexion(object) :
    def __init__(self,servidor,usuario,clave,bd):
        self.bd = pymysql.connect(servidor,usuario,clave,bd)
        self.cursor = self.bd.cursor()
        print("Conexion exitosa")
    
    def ejecutarQuery(self,sql):
        self.cursor.execute(sql)
        return self.cursor

    def cerrarConexion(self):
        self.bd.close()
        print("Base de datos cerrada")
    
    def commit(self):
        self.bd.commit()
    
    def roolBack(self):
        self.bd.rollback()
