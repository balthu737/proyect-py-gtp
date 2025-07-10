while True:
    print("""Bienvenido a tu agenda de contatas 
Aca vas a poder ver el nombre, apellido y numero de las persona
Que es lo que queres hacer??
1) Agregar contactos
2) Buscar contacto
3) Eliminar contacto
4) Listar contacto
5) Salir""")
    desicion = int(input("Elegir un numero: "))
    if desicion == 1:
        print("Agregando contacto")
    elif desicion == 2:
        print("Buscando contacto")
    elif desicion == 3:
        print("Eliminando contacto")
    elif desicion == 4:
        print("Listando contactos")
    elif desicion == 5:
        break
    else:
        print("No tenemos esa funcion")