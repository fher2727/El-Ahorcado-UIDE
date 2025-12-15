import random

PALABRAS = ["python", "programacion", "ahorcado", "logica", "ingenieria"]
MAX_INTENTOS = 6

def elegir_palabra():
    return random.choice(PALABRAS)

def mostrar_estado(palabra, letras_correctas):
    return " ".join([letra if letra in letras_correctas else "_" for letra in palabra])

def validar_entrada(letra, letras_usadas):
    if len(letra) != 1:
        return False
    if not letra.isalpha():
        return False
    if letra in letras_usadas:
        return False
    return True

def jugar():
    palabra = elegir_palabra()
    intentos = MAX_INTENTOS
    letras_correctas = set()
    letras_usadas = set()

    print("=== JUEGO DEL AHORCADO ===")

    while intentos > 0:
        estado = mostrar_estado(palabra, letras_correctas)
        print("\nPalabra:", estado)
        print("Intentos restantes:", intentos)

        if "_" not in estado:
            print("¡Ganaste!")
            return

        letra = input("Ingresa una letra: ").lower()

        if not validar_entrada(letra, letras_usadas):
            print("Entrada inválida")
            continue

        letras_usadas.add(letra)

        if letra in palabra:
            letras_correctas.add(letra)
            print("Correcto")
        else:
            intentos -= 1
            print("Incorrecto")

    print("Perdiste. La palabra era:", palabra)

jugar()

