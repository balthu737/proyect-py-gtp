def agregar():
    tarea = input("¿Qué tarea queres agregra: ")
    with open("04-to-do\\to-do.txt", "a+", encoding="UTF-8") as archivo:
        archivo.write(f'[ ] {tarea}\n')
    return f'tu tarea fue agregada con exito, esta fue: {tarea}'