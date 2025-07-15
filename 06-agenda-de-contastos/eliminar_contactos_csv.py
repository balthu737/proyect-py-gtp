import pandas as pd

def eliminar_contactos(nombre):
    try: 
        contacto = pd.read_csv("06-agenda-de-contastos\\contactos.csv")
        existe = contacto["Nombre"] == nombre
        if existe.any():
            contacto = contacto[~existe]
            contacto.to_csv("06-agenda-de-contastos\\contactos.csv", index=False)
            return f'El contacto: {nombre} fue eliminado correctamente'
        else:
            return f'El contacto: {nombre} no se encontro'
    except FileNotFoundError:
        return "No se encontro el archivo"
