import random

# Lista de palabras (puedes agregar más)
PALABRAS = [
    "ecuador", "programacion", "algoritmo", "variable",
    "ingenieria", "inteligencia", "python", "ahorcado"
]

# Dibujos por cada número de errores (0 a 6)
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


def elegir_palabra() -> str:
    """Selecciona una palabra aleatoria de la lista."""
    return random.choice(PALABRAS)


def construir_estado(palabra: str, letras_correctas: set[str]) -> str:
    """
    Crea el estado visible de la palabra.
    Ej: p y t h o n  ->  p _ t h o n (si falta la y)
    """
    # Uso de estructura repetitiva (for) con comprensión de listas
    return " ".join([c if c in letras_correctas else "_" for c in palabra])


def validar_entrada(entrada: str, letras_usadas: set[str]) -> tuple[bool, str]:
    """
    Validación completa de la entrada del usuario (parte más delicada).
    Reglas:
      1) Debe ser 1 solo carácter
      2) Debe ser una letra
      3) No debe repeti
      """
