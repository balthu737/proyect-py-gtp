from ver_tareas import ver_tareas

def completar():
    ver_tareas()
    num = int(input("Ingresa el número de la tarea a marcar como hecha: "))
    
    with open("04-to-do\\to-do.txt", "r", encoding="utf-8") as archivo:
        tareas = archivo.readlines()
    
    if 0 < num <= len(tareas):
        if "[x]" in tareas[num - 1]:
            print("La tarea ya estaba marcada como hecha.")
        else:
            tareas[num - 1] = tareas[num - 1].replace("[ ]", "[x]", 1)
            with open("04-to-do\\to-do.txt", "w", encoding="utf-8") as archivo:
                archivo.writelines(tareas)
            print("Tarea marcada como hecha.")
    else:
        print("Número inválido.")
        