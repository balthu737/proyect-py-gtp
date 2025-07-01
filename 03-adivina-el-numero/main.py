from generar_numero import generar
from adivinar import adivinar

intentos = 1
numero = generar()
while True:
    print(intentos)
    adivinar(numero)
    intentos += 1
