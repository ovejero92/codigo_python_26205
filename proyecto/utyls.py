import time
import os
from colorama import init, Fore

init()

def barra_progreso_basica():
    """Muestra una barra de progreso animada y después devuelve el control."""
    for i in range(30 + 1):
        porcentaje = int(i / 30 * 100)
        # barra = "█" * i + "░" * (30 - i)
        # barra = "⁜" * i + "░" * (30 - i)
        # barra = "💨" * i + "░" * (30 - i)
        # barra = "👣" * i + "░" * (30 - i)
        barra = "🔲" * i + "🔳" * (30 - i)
        print(Fore.BLUE + f"\r Cargando : {barra}  {porcentaje}%", end="", flush=True)
        time.sleep(2 / 30)
    print()  # salto de línea al terminar

def limpiar_consola():
    ...

