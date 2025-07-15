import pandas as pd

def buscar_contactos(nombre):
    try:
        contactos = pd.read_csv("06-agenda-de-contastos\\contactos.csv")
        buscar = contactos.loc[contactos["Nombre"] == nombre]
        return buscar
    except FileNotFoundError:
        print("No se encontro el archivo")
