def comparacion(jugadaapp):
    jugador = input("cual es tu eleccion?: ")
    app = jugadaapp
    if jugador == "tijeras" & app == "tijeras":
        return "Empate"
    elif jugador == "tijeras" & app == "piedra":
        return "Pierdes"
    elif jugador == "tijeras" & app == "papel":
        return "Ganas"
    elif jugador == "piedra" & app == "tijeras":
        return "Ganas"
    elif jugador == "piedra" & app == "piedra":
        return "Empate"
    elif jugador == "piedra" & app == "papel":
        return "Pierdes"
    elif jugador == "papel" & app == "tijeras": 
        return "Pierdes"
    elif jugador == "papel" & app == "piedra":
        return "Ganas"
    elif jugador == "papel" & app == "papel":
        return "Empate"
    else:
        return "Que haces??"