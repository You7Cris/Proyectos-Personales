## SQLITE ya viene instalado con Python, bases de datos SQL, como conectar bases de datos

#importar modulo

from itertools import product
import sqlite3

#conexion 
conexion = sqlite3.connect('19-bases-datos/pruebas.db') #base de datos con la que vamos a trabajar ingresar la direccion donde se vaya a crear cuando se ejecute

# Crear cursor /Lo que va a permitir ejecutar las consultas
cursor = conexion.cursor()


# Crear tabla
cursor.execute("""CREATE TABLE IF NOT EXISTS productos(
"id INTEGER PRIMARY KEY AUTOINCREMENT,
"titulo VARCHAR(255),
"descripcion TEXT,
"precio int(255)
);
""")

"""
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT,"+
"titulo VARCHAR(255),"+
"descripcion TEXT,"+
"precio int(255)"+
")")
"""

# Guardar cambios
conexion.commit()

# Insertar datos
"""
cursor.execute("INSERT INTO productos VALUES (null, 'Segundo producto', 'Descripcion de mi producto', 550)")
conexion.commit()
"""

# Borrar registros
cursor.execute("DELETE FROM productos")
conexion.commit()

# Insertar muchos registros de golpe
productos = [
    ("Ordenador portatil", "Buen PC", 700),
    ("PS4", "Buena consola", 800),
    ("PS3", "Buena consola", 350),
    ("Telefono movil", "Buen telefono", 560),
    ("Tablet Samsung", "Buena tablet", 600),
    ("Placa base", "Buena placa", 400),
]
cursor.executemany("INSERT INTO productos VALUES (null, ?,?,?)", productos)
conexion.commit()

#Update

cursor.execute("UPDATE productos SET precio=678 WHERE precio=350")

# Listar datos
cursor.execute("SELECT * FROM productos WHERE precio >= 500")

productos = cursor.fetchall()

for producto in productos:
    print("ID: ",producto[0])
    print("Titulo: ",producto[1])
    print("Descripcion: ",producto[2])
    print("Precio: ",producto[3])
    print("\n")

cursor.execute("SELECT titulo FROM productos;")
producto = cursor.fetchone() #Primer registro que tenga
print(producto)

# Cerrar conexion
conexion.close()