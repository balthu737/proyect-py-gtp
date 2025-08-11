import random

def jugada():
    juego = ["tijeras", "piedra", "papel"]
    juego_procedural = random.choice(juego)
    return juego_procedural