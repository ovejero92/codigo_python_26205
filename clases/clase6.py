# # # ingresos = [] # <- Lista sin datos
# # # mes = 1
# # # total = 0
# # # # == != >= > < <= 
# # # while mes <= 6: #
# # #     monto_str = input(f"Ingrese el monto del mes {mes}: ") # -FAS

# # #     es_numero_valido = (monto_str.isdigit()) or (monto_str.startswith("-") and monto_str[1:].isdigit())   # V o F monto_str.count("-") == 1
# # #     if es_numero_valido:  # F - V 
# # #         monto = int(monto_str)
# # #         if monto >= 0:
# # #             ingresos.append(monto)
# # #             total += monto
# # #             mes += 1
# # #         else:
# # #             print("no se puede poner numeros negarivos")
# # #     else:
# # #         print("NO se puede ingresar letras ni caracteres especiales")   

# # # print("\n-- Resumen Financiero --")

# # # indice = 0
# # # while indice < len(ingresos):
# # #     print(f"Mes {indice + 1}: $ {ingresos[indice]}") # 
# # #     indice += 1 

# # # mi_str = "HOLA " # <- str  ["H","O","L","A"," "]

# # # # mi_str[1] = "A"
# # # mi_str = "CHAU"
# # # #            0  1  2    3     4      5             6
# # # mi_lista = ["",13,16.7,True, "[ ] ", "otra cosa", 1233] # <- listas 
# # # mi_lista[1] = 90

# # # #Slicing [inicio : fin : paso a paso]
# # #  # -> 
# # # print(mi_lista[2:4:1])
# # # print(mi_lista[0:len(mi_lista):2])
# # # print(mi_str[0:2:1])


# # #for variable in secuencia:
# #     # Bloque de código
# # mi_lista_alumnos = ["Lucas","Javier","Noe"]

# # for alumno in mi_lista_alumnos:
# #     print(f"Alumnos n: {alumno}")

# # indice = 0
# # while indice < len(mi_lista_alumnos):
# #     print(f"alunmo n{ indice + 1 }: {mi_lista_alumnos[indice]}")
# #     indice += 1

# # # continua = True
# # while True:
# #     print("Menu")
# #     print("1.Agregar poducto")
# #     print("5.Salir")
# #     opt = int(input("Ingresa la opcion que quieras del menu (5 para salir): "))
# #     if opt == 5:
# #         # continua = False
# #         break

# # print("Saliste")


# # palabra = "Hola"
# # for letra in palabra:
# #     if letra == "l":
# #         continue
# #     print(f"Letra: ", letra)


# # productos = ["P001", "P002", "P003", "P004", "P005"]
# # producto_a_buscar = "P003"
# # for producto in productos:
# #     if producto == producto_a_buscar.upper():
# #         print("Producto encontrado:", producto)
# #         break
# #     print("Buscando...")
# # print("Fin de la búsqueda.")

# # range(inicio, fin, paso)
# # for i in range(10, -1, -2):
# #     print(i)

# # frutas = ["manzana", "banana", "naranja","anana"] 

# # for i in range(0,len(frutas),2):  # <- 0 1 2 3  -> range(0:4:1) -> len(frutas) = 4
# #     print(f"Fruta {i+1}: {frutas[i]}")

# # ingresos = [40000, 55000, 60000, 45000, 70000, 50000]
# # count = 0

# # for ingreso in ingresos:
# #     if ingreso > 50000:
# #         count += 1

# # print(f"Cantidad de ingresos superiores a $50000: {count}")

# palabra = input("Ingrese una palabra: ") # agosto
# vocales = "aeiouAEIOU"
# contador = 0

# for letra in palabra:
#     if letra in vocales:
#         contador += 1

# print(f"La palabra tiene {contador} vocales")


lista_prod = ["p1","p2","p3"]

lista_backup = lista_prod.copy()
lista_backup = lista_prod[::] # [0:len(lista_prod):1]


lista_backup.append("p4")
print(lista_prod)
print(lista_backup)