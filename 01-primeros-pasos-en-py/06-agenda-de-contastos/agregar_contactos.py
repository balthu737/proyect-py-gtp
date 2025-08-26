import pandas as pd

def agregar_contactos(Nombre):
    try:
        contactos = pd.read_csv("06-agenda-de-contastos\\contactos.csv")
        existe = contactos["Nombre"] == Nombre
        if existe.any():
            return f'Este contacto{Nombre} ya existe'
        else:
            nuevo_contacto = pd.DataFrame({
                "Nombre": [Nombre]
            })
            contactos = pd.concat([contactos, nuevo_contacto], ignore_index=True)
            contactos.to_csv("06-agenda-de-contastos\\contactos.csv", index=False)
            return f'Agregando el contacto: {Nombre}'
    except FileNotFoundError:
        return "No se encontro el archivo"
