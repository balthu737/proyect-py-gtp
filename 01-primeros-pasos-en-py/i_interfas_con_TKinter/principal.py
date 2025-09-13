import tkinter as tk
from tkinter import messagebox
from convertidor_de_unidades import app1

def eleccion():
    try:
        selecion = lista.get(lista.curselection())
        if selecion == "Convertidor de unidades":
            app1()
            #messagebox.showinfo("app", "convertidor de unidades")
        elif selecion == "Adivina el numero":
            messagebox.showinfo("app","adivina el numero")
        elif selecion == "To do":
            messagebox.showinfo("app", "to do")
        elif selecion == "Piedra papel o tijeras":
            messagebox.showinfo("app", "piedra papel tijera")
    except:
        messagebox.showwarning("atencion", "por favor selecione un opcion")
def interfaz():
    global lista
    ventana = tk.Tk()
    ventana.geometry("300x150")
    ventana.title("Seleccion de apps")
    lista = tk.Listbox(ventana,width=25, height=4)
    lista.insert(1,"Convertidor de unidades")
    lista.insert(2,"Adivina el numero")
    lista.insert(3,"To do")
    lista.insert(4,"Piedra papel o tijeras")
    lista.place(x=75, y=5)
    boton = tk.Button(ventana, text="Selecciona uno", command=eleccion)
    boton.place(x=105, y=75)
    ventana.mainloop()

interfaz()