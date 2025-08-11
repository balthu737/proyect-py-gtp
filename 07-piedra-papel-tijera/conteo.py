def conteo(resultado):
    victorias = 0
    derrotas = 0
    empates = 0 
    if resultado == "Ganas":
        victorias =+ 1 
        return victorias
    elif resultado == "Perdiste":
        derrotas =+ 1
        return derrotas
    elif resultado == "Empate":
        empates =+ 1 
        return empates