from listar_contactos import listar_contactos
from buscar_contactos import buscar_contactos
from eliminar_contactos_csv import eliminar_contactos
from agregar_contactos import agregar_contactos

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
        contacto = input("A quien queres agregar?: ")
        print(agregar_contactos(contacto))
    elif desicion == 2:
        nombre = input("A quien queres buscar?: ")
        print(buscar_contactos(nombre))
    elif desicion == 3:
        nombre = input("A quien queres eliminar?: ")
        print(eliminar_contactos(nombre))
    elif desicion == 4:
        print(listar_contactos())
    elif desicion == 5:
        break
    else:
        print("No tenemos esa funcion")