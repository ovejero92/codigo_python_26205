import random 
from colorama import init

init()

def lanzar_dado(caras_dado:int=6) -> int:
    """ Ejemplo de random - dado """
    resultado = random.randint(1,caras_dado)
    return resultado

dado_clasico = lanzar_dado()
dado_magico = lanzar_dado(12)

print(f"El numero que salió del dado clasico es: {dado_clasico}")
print(f"EL numero que salio del dado magico es : {dado_magico}")


def adivina_el_numero(numero_usuario):
    numero = random.randint(1,100)
    if numero == numero_usuario:
        print("Muy bien adivinaste")
    else:
        print("mal intenta denuevo ")



