# Instalar el comando pip install mysql-connector-pyhton

import mysql.connector

# Conexion con la base de datos
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database = "master_python"
)

# ¿La conexion ha sido correcta
# print(database)

# Cursor que permite ejecutar las consultas
cursor = database.cursor(buffered=True)

# Crear base de datos
"""
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
"""

# Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)

# Insertar datos

#cursor.execute("INSERT INTO vehiculos VALUES (null, 'Lamborghini', 'Gallardo', 35000)")

coches = [
    ('Seat', 'Ibiza',5000),
    ('Renault', 'Clio',15000),
    ('Citroen', 'Saxo', 2000),
    ('Mercedez','Clase C', 35000)
]

#cursor.executemany("INSERT INTO vehiculos VALUES ('null',%s,%s,%s)", coches)

database.commit()

cursor.execute("SELECT * FROM vehiculos WHERE precio<=5000 AND marca = 'Seat'")

result = cursor.fetchall() 

print("Todos mis coches: ")
for coche in result:
    print("Marca: ",coche[1])
    print("Modelo: ",coche[2])
    print("Precio: ",coche[3])
    print("\n")

cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone()

print(coche)

# Eliminar

cursor.execute("DELETE FROM vehiculos WHERE marca = 'Mercedez' ")
database.commit()

print(cursor.rowcount, "borrados!!") # Ver que se ha borrado

# Actualizar datos

cursor.execute("UPDATE vehiculos SET modelo='León' WHERE marca='Seat'")
database.commit()

print(cursor.rowcount, "actualizados!!")
