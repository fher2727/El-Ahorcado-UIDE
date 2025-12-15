import random

"""
Proyecto: Juego del Ahorcado
Materia: Lógica de Programación
Lenguaje: Python
Descripción:
Juego desarrollado en consola que aplica estructuras
condicionales, repetitivas y validaciones de entrada.
"""

# -------------------- CONSTANTES --------------------

PALABRAS = [
    "ecuador", "programacion", "algoritmo",
    "variable", "ingenieria", "python", "ahorcado"
]

HANGMAN = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]

MAX_ERRORES = 6

# -------------------- FUNCIONES --------------------

def elegir_palabra():
    """Selecciona una palabra aleatoria."""
    return random.choice(PALABRAS)


def construir_estado(palabra, letras_correctas):
    """
    Construye el estado visible de la palabra.
    Usa un ciclo for (estructura repetitiva).
    """
    estado = ""
    for letra in palabra:
        if letra in letras_correctas:
            estado += letra + " "
        else:
            estado += "_ "
    return estado.strip()


def validar_entrada(letra, letras_usadas):
    """
    Valida la letra ingresada por el usuario.
    """
    if len(letra) != 1:
        return False
    if not letra.isalpha():
        return False
    if letra in letras_usadas:
        return False
    return True


def mostrar_panel(palabra, letras_correctas, letras_usadas, errores):
    """Muestra el tablero del juego."""
    print(HANGMAN[errores])
    print("Palabra:", construir_estado(palabra, letras_correctas))
    print("Letras usadas:", ", ".join(letras_usadas) if letras_usadas else "-")
    print(f"Errores: {errores}/{MAX_ERRORES}")


def jugar():
    """Función principal del juego."""
    palabra = elegir_palabra()
    letras_correctas = set()
    letras_usadas = set()
    errores = 0

    print("\n=== JUEGO DEL AHORCADO ===")

    while errores < MAX_ERRORES:
        mostrar_panel(palabra, letras_correctas, letras_usadas, errores)

        # Condición de victoria
        if "_" not in construir_estado(palabra, letras_correctas):
            print("\n✅ ¡Ganaste! La palabra era:", palabra)
            return

        letra = input("Ingresa una letra: ").lower().strip()

        if not validar_entrada(letra, letras_usadas):
            print("⚠️ Entrada inválida. Intenta de nuevo.")
            continue

        letras_usadas.add(letra)

        if letra in palabra:
            letras_correctas.add(letra)
            print("✅ Correcto")
        else:
            errores += 1
            print("❌ Incorrecto")

    mostrar_panel(palabra, letras_correctas, letras_usadas, errores)
    print("\n💀 Perdiste. La palabra era:", palabra)


def menu():
    """Menú principal del programa."""
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1) Jugar")
        print("2) Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            jugar()
        elif opcion == "2":
            print("Gracias por jugar. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta otra vez.")

# -------------------- EJECUCIÓN --------------------

if __name__ == "__main__":
    menu()
