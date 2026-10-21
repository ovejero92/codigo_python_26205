
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
# print(mostrar_bienvenida(input("Ingresa tu nombre")))

def sumar_precios(precios:list) -> int | float:
    """
    """
    
    total = 0
    for precio in precios:
        
        total = total + precio
    return total

print(sumar_precios(["1500","1000","500"]))

# def calcular_area_y_perimetro(base, altura):
#     area = base * altura
#     perimetro = 2 * (base + altura)
#     return (area, perimetro)

# tupla = ("hoka","chau")

# nombre, edad , ciudad = ("gustavo", 33 , "bsas")

# b = int(input("Ingresa la base: "))
# a = int(input("Ingresa la altura: "))

# area, perimetro = calcular_area_y_perimetro(b, a)
# # ar,p = calcular_area_y_perimetro(50, 100)
# primer_dato = calcular_area_y_perimetro(b, a)

# print(f"la base es {b}, la altura es {a} y el resultado es:\narea:{area}\nperimetro:{perimetro} ")
# print(f"primer dato: {calcular_area_y_perimetro(b, a)[0]}")
# print(f"primer dato: {primer_dato[0]}")

# print(type(primer_dato))

help(print())

"""

"""
# laskjdlaskjdsakl
def calcular_iva(monto):
    """ Devuelve el IVA (21%) de un monto """
    return monto * 0.21

# help(calcular_iva)
# print(calcular_iva.__doc__)
calcular_iva()

def saludar(nombre):
    """
    Esta función saluda a la persona pasada como parámetro.
    
    Parámetros:
    nombre (str): El nombre de la persona a saludar.
    
    Retorna:
    str: El saludo personalizado.
    """
    return f"¡Hola, {nombre}!"

def calcular_total(precio:int | float, cantidad:int, descuento:int=0) -> int | float :
    """
    Calcula el total a pagar de un producto.
    Aplica el descuento (en porcentaje) sobre el subtotal y después suma
    el IVA del 21%.

    Args:
        precio (int | float): precio unitario del producto.
        cantidad (int): unidades compradas.
        descuento (int): porcentaje de descuento de 0 a 100. Por defecto 0.

    Returns:
        El total a pagar .
    """
    subtotal = precio * cantidad
    con_descuento = subtotal - subtotal * descuento / 100
    return con_descuento * 1.21

calcular_total()