# archivo = open("datos.txt", "r", encoding="UTF-8")
# # contenido = archivo.read()  -> lee todo el archivo
# # print(contendo)
# lineas = archivo.readlines()
# print(lineas)
# for linea in lineas:
#     print(linea.strip())
# archivo.close()

# archivo = open("datos.txt", "w" ,encoding="UTF-8")
# archivo.write("Hola, este es un archivo de prueba.\n")
# archivo.write("Segunda línea del archivo.\n")
# archivo.close()

# archivo = open("datos.txt", "a",encoding="UTF-8")
# archivo.write("Tercera línea del archivo.\n")
# archivo.write("cuarta línea del archivo.")
# archivo.close()

# print(contenido)

# import os   # módulo de la biblioteca estándar
# print("Python busca y crea archivos en:", os.getcwd())
# print("¿Existe datos.txt?", os.path.exists("datos.txt"))

# # if os.path.exists("datos.txt"):
# #     archivo = open("datos.txt","r")
# # else:
# #   print("el archivo no existe")

# productos = [("Yerba", 3200.50), ("Café", 5400.00), ("Azúcar", 1100.75)]
# # 1) Escribir: una línea por producto, campos separados por coma
# archivo = open("productos.txt", "w", encoding="utf-8")
# for nombre, precio in productos:
#     archivo.write(f"{nombre},{precio}\n")
# archivo.close()
# # 2) Leer: cada línea vuelve como texto, hay que convertir el precio
# archivo = open("productos.txt", "r", encoding="utf-8")
# total = 0
# for linea in archivo:
#     nombre, precio = linea.strip().split(",")
#     print(f"{nombre}: ${float(precio):.2f}")
#     total += float(precio)
# archivo.close()
# print(f"Total: ${total:.2f}")

try:
    archivo = open("datos.txt", "r")
# except OSError as e:
#     print("un error de os")
    # archivo = open("errores.log","w")
    # archivo.write("un error de os {e}")
except FileNotFoundError as err:
    print(f"Error: El archivo 'datos.txt' no existe. {err}")
    print("Verificá el nombre o la ubicación del archivo.")
else:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)
finally:
    archivo.close()
    print("Gracias por leer el archivo.")


print("=== Calculadora de División ===")
try:
    numerador = float(input("Ingresá el numerador: "))
    denominador = float(input("Ingresá el denominador: "))
    resultado = numerador / denominador
    print(f"El resultado de la división es: {resultado:.2f}")
except ValueError as err:
    print(f"[ERROR] Debés ingresar valores numéricos válidos.\nerror->{err}")
except ZeroDivisionError:
    print("[ERROR] El denominador no puede ser cero.")
    print(" Intentá nuevamente.")
except ArithmeticError:
    print("")
finally:
    print("Gracias por usar la calculadora.")

with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())

from typing import Optional

def calcular_promedio(notas: list[float]) -> Optional[float]:
    """Calcula el promedio de una lista de notas.

    Args:
        notas: Lista de notas, cada una entre 0 y 10.

    Returns:
        El promedio como float, o None si la lista está vacía.

    Raises:
        ValueError: Si alguna nota está fuera del rango 0-10.
        TypeError: Si alguna nota no es un número.
    """
    if not notas:
        return None  # Caso válido pero sin resultado: devolvemos None

    for nota in notas:
        if not isinstance(nota, (int, float)):
            raise TypeError(f"La nota {nota} no es un número.")
        if not 0 <= nota <= 10:
            raise ValueError(f"Nota inválida: {nota}. Debe estar entre 0 y 10.")

    return sum(notas) / len(notas)  # Caso normal: devolvemos el resultado


def procesar_alumno(nombre: str, notas: list[float]) -> None:
    """Calcula y muestra el promedio de un alumno manejando errores."""
    print(f"\n--- Procesando a {nombre} ---")
    try:
        promedio = calcular_promedio(notas)  # Solo lo que puede fallar
    except ValueError as error:
        print(f"Error de valor: {error}")
    except TypeError as error:
        print(f"Error de tipo: {error}")
    else:
        # Se ejecuta SOLO si no hubo excepción
        if promedio is None:
            print("El alumno no tiene notas cargadas.")
        else:
            print(f"Promedio: {promedio:.2f}")
    finally:
        # Se ejecuta SIEMPRE
        print(f"Fin del procesamiento de {nombre}.")


if __name__ == "__main__":
    procesar_alumno("Lucía", [8, 9, 7.5])     # Todo bien
    procesar_alumno("Martín", [])             # Devuelve None
    procesar_alumno("Sofía", [8, 15, 6])      # ValueError
    procesar_alumno("Tomás", [8, "diez", 6])  # TypeError