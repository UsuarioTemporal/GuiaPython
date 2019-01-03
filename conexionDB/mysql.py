import pymysql

# Mira mama, mas facil que java imposible
db =pymysql.connect("localhost", "root", "mysql","tienda_java")
print(db)



cursor = db.cursor()

cursor.execute("SELECT VERSION()")
version = cursor.fetchone()
print(version)