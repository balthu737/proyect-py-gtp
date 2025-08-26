def comparacion(jugadaapp):
    jugador = input("cual es tu eleccion?: ")
    app = jugadaapp
    if jugador == "tijeras" and app == "tijeras":
        return "Empate"
    elif jugador == "tijeras" and app == "piedra":
        return "Pierdes"
    elif jugador == "tijeras" and app == "papel":
        return "Ganas"
    elif jugador == "piedra" and app == "tijeras":
        return "Ganas"
    elif jugador == "piedra" and app == "piedra":
        return "Empate"
    elif jugador == "piedra" and app == "papel":
        return "Pierdes"
    elif jugador == "papel" and app == "tijeras": 
        return "Pierdes"
    elif jugador == "papel" and app == "piedra":
        return "Ganas"
    elif jugador == "papel" and app == "papel":
        return "Empate"
    else:
        return "Que haces??"

