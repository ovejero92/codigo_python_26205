# saludo = ""
# def saludar():
#     global saludo
#     saludo = "Hola como estan?"
#     # print(saludo)
# def adios():
#     global saludo
#     saludo = "chau"
# print(saludo)  # -> ""
# saludar()
# print(saludo)  # "Hola como estan?"
# adios()
# print(saludo) # -> "chau"



# def saludar():
#     print("hola")

# saludar()
# saludar()
# saludar()
# saludar()


# def saludar(nombre):
#     print(f"¡Hola, {nombre}!")

# saludar(156)
# saludar("Luis")
# res= ""
def sumar(a,b):
    total = a + b
    print(total)
    # global res
    # res = total

sumar(5,10)
def res(a,b):
    total = a - b
    print(total)
res(5,10) 

# print(res)
def header(mensaje):
    print("="*40 )
    print(f"--- {mensaje} ---")
    print("="*40 )

def menu():
    header("Sistema de gestión de productos")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

while True:
    menu()

    opt = input()

    if opt == "1":
        header("agregar productos")
    
    if opt == "5":
        break

while True:
    menu()