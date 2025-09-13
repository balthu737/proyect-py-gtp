def cantidad_de_lineas(ruta):
    try:
        with open(ruta, "r", encoding="UTF-8") as archivo:
            lineas = archivo.readlines()
            cantidad = len(lineas)
        return f'la cantidad de lineas es: {cantidad}'
    except FileNotFoundError:
        return f'salame el archivo {ruta} no exite'
    

print(cantidad_de_lineas("05-analizador-de-textos\\prueba.txt"))
