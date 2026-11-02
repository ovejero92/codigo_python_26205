
import os
import sys
import time


# ============================================================
# MODULO OS - Interactuar con el sistema operativo
# ============================================================

# Devuelve la ruta del directorio de trabajo actual
ruta = os.getcwd()
print("Directorio actual:", ruta)

# Lista nombres de archivos y carpetas de una ruta
print(os.listdir(ruta))  # Usando una variable con la ruta
print(os.listdir("."))   # Usando "." para indicar la carpeta actual

# Comprueba si existe un archivo o una carpeta
print(os.path.exists("main.py"))

# Comprueba si una ruta corresponde a un archivo o una carpeta
print(os.path.isfile("main.py"))
print(os.path.isdir("."))

# Crea una carpeta
# Si ya existe, os.mkdir() genera un error
if not os.path.exists("backup"):
    os.mkdir("backup")

# Crea carpetas anidadas
# exist_ok=True evita el error si la carpeta ya existe
os.makedirs("backup/2026", exist_ok=True)

# Une rutas utilizando el separador correcto del sistema operativo
ruta_archivo = os.path.join("backup", "2026", "ventas.txt")
print("Ruta del archivo:", ruta_archivo)

# Obtiene el nombre del archivo a partir de una ruta
print(os.path.basename(ruta_archivo))  # ventas.txt

# Obtiene la carpeta que contiene al archivo
print(os.path.dirname(ruta_archivo))   # backup/2026

# Divide una ruta en carpeta y nombre de archivo
print(os.path.split(ruta_archivo))

# Obtiene la extensión de un archivo
print(os.path.splitext("informe.pdf"))  # ('informe', '.pdf')

# Consulta el nombre del sistema operativo
print("Sistema:", os.name)  # nt en Windows; normalmente posix en Linux/macOS

# Muestra el separador de rutas del sistema operativo
print("Separador:", os.sep)

# Consulta una variable de entorno
print("Usuario:", os.getenv("USERNAME"))  # Habitual en Windows
# En Linux/macOS se suele consultar con os.getenv("USER")

# Muestra las variables de entorno disponibles
# Puede generar una salida extensa; usalo solo si lo necesitás
# print(os.environ)

# Cambia el directorio de trabajo
# ATENCION: afecta las rutas relativas utilizadas después
# os.chdir("backup")
# print(os.getcwd())

# Elimina un archivo existente
# ATENCION: descomentá solo si querés borrar este archivo
# os.remove("backup/2026/ventas.txt")

# Elimina una carpeta vacía
# ATENCION: descomentá solo si la carpeta está vacía
# os.rmdir("backup/2026")


# ============================================================
# MODULO SYS - Información del intérprete de Python
# ============================================================

# Muestra la versión completa de Python
print("Versión de Python:", sys.version)

# Muestra la versión en componentes separados
print("Versión por componentes:", sys.version_info)

# Muestra la ruta del ejecutable de Python que está corriendo
print("Ejecutable de Python:", sys.executable)

# Muestra las rutas donde Python busca módulos para importar
print("Rutas de búsqueda de módulos:")
for ruta_modulo in sys.path:
    print(ruta_modulo)

# Muestra los argumentos recibidos desde la terminal
# El primer elemento suele ser el nombre o la ruta del script
print("Argumentos:", sys.argv)

# Ejemplo:
# Si ejecutamos: python main.py hola 123
# sys.argv contendrá algo parecido a:
# ['main.py', 'hola', '123']

# Cantidad de argumentos recibidos, incluido el nombre del script
print("Cantidad de argumentos:", len(sys.argv))

# Consulta la plataforma en la que se ejecuta Python
print("Plataforma:", sys.platform)

# Muestra el tamaño máximo de un entero según la representación
# utilizada por sys.maxsize (no es el máximo entero de Python)
print("Sys maxsize:", sys.maxsize)

# Muestra el texto de error estándar
# Normalmente se utiliza para imprimir errores
# sys.stderr.write("Este es un mensaje de error\n")

# Finaliza el programa inmediatamente con un código de salida
# 0 suele indicar que terminó correctamente
# sys.exit(0)
# ATENCION: si descomentás esta línea, no se ejecutará lo que sigue


# ============================================================
# MODULO TIME - Trabajar con el tiempo
# ============================================================

# Devuelve los segundos transcurridos desde la época Unix
# (1970-01-01 UTC)
print("Timestamp actual:", time.time())

# Muestra la fecha y hora local en formato legible
print("Fecha y hora local:", time.ctime())

# Convierte una cantidad de segundos en una pausa
# El programa espera 2 segundos antes de continuar
# print("Esperando...")
# time.sleep(2)
# print("Continuamos después de 2 segundos")

# Obtiene la fecha y hora local como una estructura de datos
fecha = time.localtime()
print("Año:", fecha.tm_year)
print("Mes:", fecha.tm_mon)
print("Día:", fecha.tm_mday)
print("Hora:", fecha.tm_hour)
print("Minuto:", fecha.tm_min)
print("Segundo:", fecha.tm_sec)

# Convierte la fecha y hora a un formato personalizado
print(time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()))

# Algunos códigos de formato:
# %d = día
# %m = mes
# %Y = año con cuatro dígitos
# %H = hora en formato de 24 horas
# %M = minutos
# %S = segundos

# Convierte una fecha en texto a una estructura de tiempo
fecha_texto = "25/12/2026"
fecha_parseada = time.strptime(fecha_texto, "%d/%m/%Y")
print("Fecha convertida:", fecha_parseada)

# Mide cuánto tarda en ejecutarse una operación
inicio = time.perf_counter()

# Simulamos una tarea que tarda un poco
time.sleep(1)

fin = time.perf_counter()
print("Tiempo transcurrido:", round(fin - inicio, 2), "segundos")

# Compara la hora local con UTC
print("Hora UTC:", time.strftime("%d/%m/%Y %H:%M:%S", time.gmtime()))


def barra_progreso_basica():
    """Muestra una barra de progreso animada y después devuelve el control."""
    for i in range(30 + 1):
        porcentaje = int(i / 30 * 100)
        # barra = "█" * i + "░" * (30 - i)
        # barra = "⁜" * i + "░" * (30 - i)
        # barra = "💨" * i + "░" * (30 - i)
        # barra = "👣" * i + "░" * (30 - i)
        barra = "🔲" * i + "🔳" * (30 - i)
        print(f"\r Cargando : {barra}  {porcentaje}%", end="", flush=True)
        time.sleep(2 / 30)
    print()  # salto de línea al terminar

barra_progreso_basica()
