from limpiar import limpiar
from collections import Counter

def separar_y_contar(ruta):
    texto_limpio = limpiar(ruta)
    palabras = texto_limpio.split()
    contador = Counter(palabras)
    return contador
