import random
from comparacion import comparacion
from conteo import conteo
from jugada import jugada

while True:
    jugada_v = jugada()
    resultado = comparacion(jugada_v)
    conteo_v = conteo(resultado)
    print(conteo_v)
    deseo = input("Deseas ver la eleccion de la maquina? s/n: ")
    if deseo == "s":
        print(jugada_v)
    elif deseo == "n":
        continue
    else:
        print("Esa opcion no se")
    salir = input("Queres salir s/n: ")
    if salir == "s":
        break
    elif salir == "n":
        continue
    else:
        print("Esa opcion no se encuentra")
