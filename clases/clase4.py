

# nota = int(input("Pone la nota que te sacaste:"))

# if nota >= 90:
#     print("Excelente")
# elif nota >= 70:
#     print("Muy bien")
# elif nota >= 60:
#     print("Aprobado")
# else:
#     print("Reprobado")

# edad = 19

# if edad > 18:  #F
#     nombre = input("asda")

#     if nombre == "luciano": #V
#         print("Hola luciano como estas?") #<-
#     elif nombre == "lucas": #F
#         print("Hola lucas")
#     else: 
#         print("no estas en el curso de python inicial") # <-
# else:
#     print("tenes que ser mayor de 18.")


# dia_usuario = input("¿En que dia estas?").lower()  # <- dato del usuario   dia = GuStavo 
# dia_min = dia_usuario.lower()  # <- dia = gustavo

# match dia_min:
#     case "lunes":
#         print("Inicio de semana")
#     case "martes":
#         print("Segundo dia vamos que se puede")
#     case "miercoles":
#         print("mitad de semana, cerveza de regalo")
#     case "jueves":
#         print("estamos en juernes ya casi estamos en el finde.")
#     case "viernes":
#         print("En unas horas dejas de trabajar")
#     case "sabado":
#         print("Por fin sabado a difrutar")
#     case "domingo":
#         print("Disfruta lo poco que queda.")
#     case _:
#         print("No existe ese dia!")


dia = input("¿En que dia estas?")
dia = dia.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")

match dia.lower():
    case "lunes" | "martes" | "miercoles" | "jueves":
        print("Dia laboral")
    case "viernes" | "sabado" | "domingo":
        print("Fin de semana")
    case _:
        print("No existe ese dia!")

# if dia == "lunes" or dia == "martes" or dia == "jueves":
#     print("Dia laboral")
# elif dia == "viernes" or dia == "sabado" or dia == "domigno":
#     print("Fin de semana")
# else:
#     print("No existe ese dia de la semana.")


# edad = int(input("ingresa tu edad"))

# match edad:
#     case e if e > 13 and e <= 15:  # 14
#         print("Niño")
#     case e if e > 15 and e < 18:
#         print("adolescente")

texto = "          Hola Mundo                 ".strip().lower()

texto_curado = texto.lower().strip()
print(texto_curado)
# Salida: Hola Mundo

# print(texto)

texto = "Hola Mundo"   
print(texto.replace("Mundo", "Python"))
# Salida: Hola Python


texto = "AVION"   
print(texto.startswith("AV")) 
# Salida: True


texto = "Hola python como estan?"   
print(texto.find("como"))  # -> 

texto = "123"   
print(texto.isdigit())
# Salida: True

edad_str = input("ingresa tu edad:")

if edad_str.isdigit():
    edad = int(edad_str)
    if edad > 18:  #F
        nombre = input("asda")

        if nombre == "luciano": #V
            print("Hola luciano como estas?") #<-
        elif nombre == "lucas": #F
            print("Hola lucas")
        else: 
            print("no estas en el curso de python inicial") # <-
    else:
        print("tenes que ser mayor de 18.")
else:
    print("tiene que ser un nuemero")

