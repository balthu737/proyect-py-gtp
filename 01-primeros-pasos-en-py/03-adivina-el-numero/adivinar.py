
def adivinar(RandomNumber):
    respuesta = int(input("¿En que numero estoy pensando?: "))
    diferencia = abs(RandomNumber-respuesta)

    if respuesta == RandomNumber:
        print("¡¡¡FELICITACIONES GANASTE!!!")
    elif respuesta < RandomNumber:
        print("Estas por debajo")
        if diferencia <= 5:
            print("Estas cerca")
        elif diferencia <= 10:
            print("Cerca")
        elif diferencia <= 20:
            print("algo lejos")
        elif diferencia > 20:
            print("lejos")
        else :
            print("Que haces?")
    elif respuesta > RandomNumber:
        print("te pasaste")
        if diferencia <= 5:
            print("Estas cerca")
        elif diferencia <= 10:
            print("Cerca")
        elif diferencia <= 20:
            print("algo lejos")
        elif diferencia > 20:
            print("lejos")
        else :
            print("Que haces?")
    else :
        print("Eso es un numero??")

