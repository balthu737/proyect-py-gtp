def limpiar(ruta):
    try: 
        with open(ruta, "r", encoding="UTF-8") as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        print("No hay un archivo, sos un salame")
    
    conte_limpio = contenido.lower().strip()
    return f'Ya limpie tu texto esto es lo que nos quedo: {conte_limpio}'

