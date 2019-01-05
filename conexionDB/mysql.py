import pymysql

# Mira mama, mas facil que java imposible
db =pymysql.connect("localhost", "root", "mysql","tienda_java")
print(db)


# objeto cursor para consultar la version de MySQL

cursor = db.cursor() 

cursor.execute("SELECT VERSION()")
version = cursor.fetchone()
print(version)

# consultan descripcion
cursor.execute("DESC usuarios")
description = cursor.fetchone()
print(description)


# consultando registros
cursor.execute("SELECT * FROM usuarios")
consulta = cursor.fetchone()
# print(consulta)

# instarnado
# cursor.execute("INSERT INTO usuarios(nombre_usuario,correo,dni_usuario) VALUES('thom','asdasdasderwewee','12345678')")

db.commit()
cursor.execute("SELECT * FROM usuarios")
datos = cursor.fetchall()

for data in datos :
    print(data[0])
    print(data[1])
    print(data[2])