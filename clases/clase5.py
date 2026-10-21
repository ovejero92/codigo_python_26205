
# contador = 5

# while contador > 0:
#     print("Este es el intento número",contador)
#     contador -= 1
# #    contador_sumado = contador + 1

# print("")
# print("FIn")

# nombre = ""

# while nombre == "":    # ""
#    nombre = input("Ingresá tu nombre: ").strip()
#    if nombre == "":
#        print("El nombre no puede estar vacío. Intentá de nuevo.")

# condicion = True

# while condicion:
#     edad_str = input("Ingresa tu edad")
#     if edad_str.isdigit():
#         edad= int(edad_str)
#         condicion = False
#     else:
#         print("tenes que poner numeros")
    

# print(f"¡Hola, {nombre}! Gracias por ingresar tu nombre y tu edad que es: {edad}.")

# intentos = 0
# max_intentos = 3
# nombre = ""
# while intentos < max_intentos and nombre == "":
#    nombre = input("Ingresá tu nombre de usuario: ").strip()
#    if nombre == "":
#        print("El nombre no puede estar vacío. Intentá de nuevo. intento numero:",intentos+1 )
#        intentos += 1
# if nombre != "":
#    print(f"Bienvenido/a, {nombre}!")
# else:
#    print("Se agotaron los intentos. Intente más tarde.")

# numero = 0
# print("Ingresá números positivos para sumarlos. Ingresá 0 para terminar.")
# suma = 0 
# while True:
#    # Solicitamos al usuario un número
#    numero_str = input("Ingresá un número: ")
#    if numero_str.isdigit(): # " asdasd o %&#$#$ o - "
#        numero = int(numero_str)
#    else:
#        print("No se puede poner letras o caracteres especiales o numeros negativos" )
#        continue
#    # Verificamos si el número es negativo
# #    if numero < 0:
# #        print("El número es negativo, se ignora. Intentá de nuevo.")
# #        continue  
#    if numero == 0:
#        break
#    suma += numero
# print(f"La suma de los números positivos es: {suma}")

# list()

lista_de_numeros = [45,14,10,0] #  <- 

lista_mix = ["Tri",24,True,15.43]

dato = "algo"
# dato = "asdkasljdlaskdjas"
# dato[2] = "t" 
print(dato[2]) # g

lista_mix[2] = "otra cosa"
# lista_mix[0][1] = "d"

print(lista_mix[0][1]) # True

pj1 = []


nombre = input("Ingresa el nombre del pj1: ").strip()
pj1.append(nombre)
# pj1[0]= nombre   ERROR

edad = int(input("Ingresa la edad del pj1: "))
pj1.append(edad)


vida = float(input("ingresa la vida del pj1:"))
pj1.insert(1,vida)

# pj1.extend()
#[nom,edad]
print(pj1)

lista_verduras = ["papa","cebolla"]
lista_frutas = ["manszana","baj"]

lista_frutas.extend(lista_verduras)
lista_verduras.remove("papa")
# print(type(lista_mix))