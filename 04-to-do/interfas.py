from crear_tarea import agregar
def interfas():
    print("""Bienvenido a la interfase del To Do en el bloc de notas
Elegir que es lo que queres hacer:
1) Agregar tareas
2) Eliminar tareas
3) Marcas tareas""")
    decicion = int(input("Seleccionar: "))
    if decicion == 1:
        print(agregar())
    elif decicion == 2:
        return "Ejecutando 2"
    elif decicion == 3:
        return "Ejecutando 3"
    else :
        return "No tenemos esa funcion todavia"

