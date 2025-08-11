import random
from comparacion import comparacion
from conteo import conteo
from jugada import jugada

while True:
    jugada_v = jugada()
    resultado = comparacion(jugada_v)
    conteo_v = conteo(resultado)
    print(resultado)
    print(conteo_v)
    print(jugada_v)
    salir = input("Queres salir s/n: ")
    if salir == "s":
        break
    elif salir == "n":
        continue
    else:
        print("Esa opcion no se encuentra")
