# import sqlite3

# conn = sqlite3.connect(":memory:")
# cur = conn.cursor()

# cur.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY , nombre TEXT, password TEXT, rol TEXT) ")
# # cur.execute("INSERT INTO usuarios (nombre,password,rol) VALUES (?,?,?)", () )
# cur.executemany("INSERT INTO usuarios (nombre,password,rol) VALUES (?,?,?)", [ ("admin","S3cr3tA","admin"), ("eduardo","edu_el_mejor","user")  ] )

# def login_inseguro(nombre, password):
#     # CRUD - R
#     query = f"SELECT * FROM usuarios WHERE nombre = '{nombre}' AND password = '{password}'"
#     print("SQL ejecutado:", query)
#     return cur.execute(query).fetchone()

# def login_seguro(nombre, password):
#     return cur.execute(
#         "SELECT * FROM usuarios WHERE nombre = ? AND password = ?",
#         (nombre, password),
#     ).fetchone()

# print(login_inseguro("admin","cualquiera"))  # -> X
# print(login_inseguro("admin' --", "x"))  # -> 
# print(login_inseguro("x","' OR '1'='1"))  # ->
# print(login_seguro("admin' --", "x")) # ->

import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""
        CREATE TABLE cuentas (
            id INTEGER PRIMARY KEY , 
            titular TEXT NOT NULL, 
            saldo INTEGER NOT NULL CHECK (saldo >= 0)
            ) 
        """)

conn.executemany("INSERT INTO cuentas (titular, saldo) VALUES (?, ?)",
                 [("Lucas", 100), ("Ludmila", 0)])
conn.commit()

def ver_saldo(titulo):
    print(f"{titulo} - {conn.execute("SELECT titular, saldo FROM cuentas").fetchall() } ")

def transferir_mal(origen,destino,monto):
    conn.execute("UPDATE cuentas SET saldo = saldo + ? WHERE id = ?", (monto, destino))  
    conn.execute("UPDATE cuentas SET saldo = saldo - ? WHERE id = ?", (monto, origen)) 

try:
    transferir_mal(1,2,500)
except sqlite3.IntegrityError  as e:
    print("error:", e)

ver_saldo("Sin rollback")

conn.rollback()
ver_saldo("Con rollback")

def transferir(origen,destino,monto):
    try:
        conn.execute("UPDATE cuentas SET saldo = saldo + ? WHERE id = ?", (monto, destino))  
        conn.execute("UPDATE cuentas SET saldo = saldo - ? WHERE id = ?", (monto, origen))        
        print("Transferencia OK")
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        print("Transferencia  cancelada: ", e)
    finally:
        conn.close()

transferir(1,2,500)
ver_saldo("Con rollback")
transferir(1,2,60)
ver_saldo("Transferencia valida")

try:
    with conn:
        conn.execute("UPDATE cuentas SET saldo = saldo + ? WHERE id = ?", (monto, destino))  
        conn.execute("UPDATE cuentas SET saldo = saldo - ? WHERE id = ?", (monto, origen))      
except sqlite3.Error as e:
    print("eror:",e)


from contextlib import closing

with closing(sqlite3.connect(":memory:")) as conn:
    with conn:
        try:
            conn.execute(...)
        except sqlite3.Error as e:
            print("error:", e)