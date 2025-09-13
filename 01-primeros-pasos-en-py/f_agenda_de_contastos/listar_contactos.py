import pandas as pd

def listar_contactos():
    try:
        contactos = pd.read_csv("06-agenda-de-contastos\\contactos.csv")
        return contactos
    except FileNotFoundError:
        print("Archivo no encontrado.")
