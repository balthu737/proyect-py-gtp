marcador = {"victorias": 0, "derrotas": 0, "empates": 0}

def conteo(resultado):
    if resultado == "Ganas":
        marcador["victorias"] += 1
    elif resultado == "Pierdes":
        marcador["derrotas"] += 1
    elif resultado == "Empate":
        marcador["empates"] += 1

    return f'''
Tus victorias son: {marcador["victorias"]}
Tus derrotas son: {marcador["derrotas"]}
Tus empates son: {marcador["empates"]}
    '''
