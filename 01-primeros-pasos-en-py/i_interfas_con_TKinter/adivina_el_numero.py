import tkinter as tk
from c_adivina_el_numero import main

def adivina():
    app = tk.Tk()
    app.geometry("500x500")
    app.title("Adivina el numero")
    texto = tk.Label(app, text="Escribi un numero del 1 al 100")
    texto.grid()
    entrada = tk.Entry(app)
    entrada.grid()
    resultado = tk.IntVar()
    salida = tk.Label(app, textvariable=resultado)
    salida.grid()
    def numero():
        numerito = int(entrada)
        resultado.set(f"{numerito} si es")
    boton = tk.Button(app, text="Adivinaste?", command=numero)
    boton.grid()
    app.mainloop()

#adivina()
print(main.juego())