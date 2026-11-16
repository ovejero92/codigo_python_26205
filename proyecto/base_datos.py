import sqlite3

conexion = sqlite3.connect("tienda.db")
# conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL)
''')
# conexion.cursor().execute(""" 
#     CREATE TABLE IF NOT EXISTS productos (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         nombre TEXT NOT NULL,
#         precio REAL NOT NULL
#         )
# """)
# conexion.commit()
# nombre_producto = input("ingresa el nombre del producto: ")
# cursor.execute('''
#     INSERT INTO productos (nombre, precio)
#     VALUES (?, ?)
#     ''', ("lapiz", 25.50)  )
# conexion.commit()

# cursor.execute('''
#     INSERT INTO usuarios (nombre, email)
#     VALUES (?, ?)
#     ''', ("Lápiz", 25.50)  )
# conexion.commit()

# lista = []
# for lis in lista:
#     print(lis)


# cursor.execute('SELECT * FROM productos')
# productos = cursor.fetchall()
# # for producto in productos:
# #     print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]:.2f}")
# # # print(productos)

# cursor.execute("SELECT nombre,precio FROM productos WHERE precio > ? ORDER BY precio DESC",( 10, ) )
# for nombre,precio in cursor.fetchall():
#     print(f"{nombre}:{precio}")


# nuevo_precio = 250.0
# id_producto = 1
# cursor.execute('UPDATE productos SET precio = ? WHERE id = ?', (nuevo_precio, id_producto))
# conexion.commit()


nombre_producto = "Lápiz"
cursor.execute("DELETE FROM productos WHERE nombre = ?", (nombre_producto,))
conexion.commit()


print("Conexión establecida exitosamente.")
conexion.close()

