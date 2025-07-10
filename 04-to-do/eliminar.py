from ver_tareas import ver_tareas

def quitar():
    ver_tareas()
    num = int(input("Ingresa el número de la tarea a eliminar: "))
    
    with open("04-to-do\\to-do.txt", "r", encoding="utf-8") as archivo:
        tareas = archivo.readlines()
    
    if 0 < num <= len(tareas):
        tarea_eliminada = tareas.pop(num - 1)
        with open("04-to-do\\to-do.txt", "w", encoding="utf-8") as archivo:
            archivo.writelines(tareas)
        print(f"Tarea eliminada: {tarea_eliminada.strip()}")
    else:
        print("Número inválido.")
