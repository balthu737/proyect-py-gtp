def ver_tareas():
    try:
        with open("04-to-do\\to-do.txt", "r", encoding="utf-8") as archivo:
            tareas = archivo.readlines()
            if not tareas:
                print("No hay tareas.")
            else:
                for i, tarea in enumerate(tareas, 1):
                    print(f"{i}. {tarea.strip()}")
    except FileNotFoundError:
        print("El archivo aún no existe, se creará al agregar tareas.")

ver_tareas()
