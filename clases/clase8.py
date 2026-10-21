
# productos = {
#    "manzana": 150,
#    "banana": 120,
#    "naranja": 180,
   
# }
# productos["banana"] = 200
# productos["mandarina"] = 130 # pares


# buscar = input("busca en el diccionario: ")

# print(productos.get(buscar,None))

# if productos.get(buscar) == None:
#     print("el producto que estas buscando no existe")
#     buscar = input("busca en el diccionario: ")


# print(productos["kiwi"])

# tienda = {
# }
# mi_lista = [
#     "Lucas",
#     "Emiliano",
#     "Diego"
#     ] # i

# mi_lista[1]
# mi_tupla = ()


mi_dic = { 
    "nombre": ["Ana","luis","pedro"], 
    "edad": 25,  
    "ciudad": "Buenos Aires"   
    } # pares

del mi_dic["edad"]

# mi_dic["altura"] = 1.7
datos_agregados = {"altura":1.7,"localidad":"San Martin"}
datos_agregados_lista = [("edad", 1.7),("localidad","San Martin")]
mi_dic.update(datos_agregados_lista)

# valor_eliminado = mi_dic.pop("edad")   ->  25
# valor_eliminado = mi_dic.pop("datos")

valor_eliminado = mi_dic.popitem() 
print(valor_eliminado)
datos = list(mi_dic.items())
# mi_dic.keys()[0]

casteo_keys = list(mi_dic.keys())

print(casteo_keys[1])
print(mi_dic.items())


for i in range(len(datos)):   # <- 0 1 2
    print(f"key: {datos[i][0]} - value: {datos[i][1]}")

for clave, valor in mi_dic.items():  # -> [ ("nombre","Ana"), ("edad",27) ]
    print(f"{clave}: {valor}")
# lista = [ ("a",1) , ("b",2), ("c",3) ,"#"]


# dic_vacio = dict(lista) # {}
# lis_vacio = list()
# tup_vacio = tuple(lista)

# numero = int("34") # ->  34
# transformar_cadena_texto = str(numero)  # " 34"

# print(dic_vacio)

tienda = [
    {"nombre":"mouse","precio":5000,"stock":50},
    {"nombre":"mouse","precio":5000,"stock":50},
    {"nombre":"mouse","precio":5000,"stock":50},
    {"nombre":"mouse","precio":5000,"stock":50},
    {"nombre":"mouse","precio":5000,"stock":50}
]
