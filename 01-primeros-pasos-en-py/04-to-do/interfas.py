from crear_tarea import agregar
from completadas import completar
from eliminar import quitar

def interfas():
    while True:
        print("""Bienvenido a la interfase del To Do en el bloc de notas
Elegir que es lo que queres hacer:
1) Agregar tareas
2) Eliminar tareas
3) Marcas tareas
4) Salir""")
        decicion = int(input("Seleccionar: "))
        if decicion == 1:
            print(agregar())
        elif decicion == 2:
            print(quitar())
        elif decicion == 3:
            print(completar())
        elif decicion == 4:
            break
        else :  
            return "No tenemos esa funcion todavia"