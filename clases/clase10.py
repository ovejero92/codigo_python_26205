
# def saludar(nombre, apellido=""):
#     nombre_normalizado = nombre.title()
#     apellido_normalizado = apellido.title()
#     if nombre == "tri" or nombre == "gus":
#         print(f"¡Hola, profe {nombre_normalizado} {apellido_normalizado}!") 
#     else:
#         print(f"¡Hola, alumno/a {nombre_normalizado} {apellido_normalizado}!") 
#     # print("chau")

# saludar("pedro")  # Llamada a la función
# # nombre_usuario = input("Ingresa tu nombre")
# # saludar(nombre_usuario)
# saludar("lucas","lippy")
# saludar(apellido="ovejero", nombre="gustavo")

# saludar(24)
# def mostrar_bienvenida():
#     print("Bienvenido al programa")
#     print("Versión 1.0")

# mostrar_bienvenida()
# x = 0
# isActive = True
# def funcion_local():
#     local = ""
#     global x
#     x = [10,20]
#     print(f"Dentro de la función: {x}, {local}")

# def credenciales(usuario,contra):
#     global isActive
#     isActive = False

# def pago(link_de_pago):
#     global isActive
#     isActive = True

# credenciales("X","Y")
# pago("aslkdjklj12k3lj12lk4j3jh2k4")

# print(isActive)


# funcion_local()
# print(x)  # Esto daría error
# # def main():
# #     ...
# print(funcion_local())

def calcular_precio_final(precio,impuesto):
    # precio_final = precio + (precio * impuesto / 100)
    return precio + (precio * impuesto / 100) # int

print(calcular_precio_final(1000,10))
# def calcular_precio_final(precio, impuesto):
#     return precio + (precio * impuesto / 100)

def mostrar_bienvenida(n):
    if n == "gus":
        return f"Bienvenido al programa, profe {n}"
    else:
        return f"Bienvenido al programa, {n}" # str

    # print("Versión 1.0")

# n_u = input("Ingresa tu nombre")
# mostrar_bienvenida(input("Ingresa tu nombre"))
print(mostrar_bienvenida(input("Ingresa tu nombre")))

def sumar_precios(precios):
    total = 0
    for precio in precios:
        total = total + precio
    return total

print(sumar_precios([1500,1000,500]))