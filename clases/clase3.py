# print(ord('A'))

# if condicion:
    

# numero = -5
# if numero > 0:
#     print("El número es positivo.")
# else:
#     print("El número no es positivo.")

 #   T                   T
# if (edad >= 18) and ((vive_en == "CABA") or (vive_en == "Caba") ):
#     print("Sos mayor de edad.")
#     print("Y vivis en CABA")
# else:
#     print("Sos menor de edad.")
#     print("y no vivis en CABA")

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    vive_en = input("Donde vivis: ")
    print("Sos mayor de edad.")
    if vive_en == "CABA" or vive_en == "Caba" or vive_en == "caba":
        print("Y vivis en CABA")
    else:
        print("no vivis en CABA")
else:
    print("Sos menor de edad.")

# nombre = input("ingresa tu nombre: ")
# contra = input("ingresa tu contra: ")

# if nombre == "gus" and contra == "123":
#     print(" hola gus")
#     print("admin")
# else:
#     print("Hola invirado",nombre)

esta_lloviendo = False

if not esta_lloviendo:
    print("esta soleado")
else:
    print("esta lloviendo")


if esta_lloviendo == True:
    print("esta lloviendo")
else:
    print("esta soleado")

