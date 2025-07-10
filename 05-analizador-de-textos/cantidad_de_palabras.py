def cantidad_de_palabras(ruta):
    try:
        with open(ruta, "r", encoding="UTF-8") as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        print(f'salame el archivo {ruta} no exite')
    
    palabras = contenido.split()
    cantidad = len(palabras)
    return f'la cantidad de palabras es: {cantidad}'