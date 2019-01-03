import pymysql

# Mira mama, mas facil que java imposible
db =pymysql.connect("localhost", "root", "mysql","tienda_java")
print(db)


# objeto cursor para consultar la version de MySQL

cursor = db.cursor()

cursor.execute("SELECT VERSION()")
version = cursor.fetchone()
print(version)

cursor.execute("DESC usuarios")
description = cursor.fetchone()
print(description)