# ventas = [1,2,3]
# ventas2 = [4,5,6]   

# fusionadas = [ventas,ventas2]
# # ventas2.extend(ventas)
# fusionadas2 = ventas + ventas2

# ventas.append([5,6,7,8])
# fusionadas2[2] = 13


# print(ventas)  
# print(ventas2)
# # Salida: [1,2,3,100]

# print(fusionadas2)

# ventas = []
# nombre = []
# while True:
#     nombre_prod = input("ingresa el nombre del producto (pone 0 para salir): ")
#     if nombre_prod == "0":
#         break
#     monto = input("ingresa el monto del producto: ") # "34" , "25" -> 3425
#     if monto.isdigit():
#         monto = int(monto)
#         nombre.append(nombre_prod)
#         ventas.append(monto)
#     else:
#         print("ingresa un numero valido positivo")
# for monto in ventas:
#     print(monto)
# for i in range(len(ventas)):  # -> range(5) -> range(inicio,final,saltos) 0 1 2 3 4
#     print(f"{nombre[i]} : ${ventas[i]}")

# ventas=[]
# nombre=[]
# while True:
#     nombre_prod = input("ingresa el nombre del producto (pone 0 para salir): ")
#     if nombre_prod == "0":
#         break
#     monto = input("ingresa el monto del producto: ")
#     if monto.isdigit():
#         monto = int(monto)
#         nombre.append(nombre_prod)
#         ventas.append(monto)
#     else:
#         print("Ingresa un numero valido positivo")
# # for monto in ventas:
# #     print(monto)    
# for i in range(len(ventas)):
#     print(f"{nombre[i]} : ${ventas[i]}")


# lista_alumnos = ["Lucas","Malvina","Francisco","Matias","Franco"]

# busqueda = input("Pone el nombre del alumno que estas buscando para sacar de la lista: ")

# index_alumno = lista_alumnos.index(busqueda)  # Lucas -> 0

# alumno_eliminado = lista_alumnos.pop(index_alumno)

# opt = input(f"Estas seguro que queres eliminar a {alumno_eliminado}")
# if  opt == "no":
#     lista_alumnos.insert(index_alumno,alumno_eliminado)

# print(index_alumno)
# print(lista_alumnos)


nombre,edad,altura = ("gus",33,1.67)

mi_tupla = ("gus",33,1.67)

mi_tupla2 = "gus",
mi_tupla2 = ("gus",)
mi_lista = ["gus"]

mi_lista[0] = "Tri"
# mi_tupla[1] = 34

tupla_colores = ("#fff","#000",)
tupla_colores2 = ("blue","ref")

tupla_colores = ""

print(tupla_colores)