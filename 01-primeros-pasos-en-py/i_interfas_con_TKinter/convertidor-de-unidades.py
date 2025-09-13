import tkinter as tk
import sys 
sys.path.append("C:\Users\balth\OneDrive\Desktop\py\01-primeros-pasos-en-py\b_convertidor_de_unidades")
from b_convertidor_de_unidades import Celfa, Facel
from b_convertidor_de_unidades import KmMilla, MillaKm

def app1():
    app = tk.Tk()
    app.geometry("500x500")
    app.title("Convertido de unidades")
    opcion = tk.IntVar()
    label = tk.Label(app, text="¿Qué queres calcular?")
    label.grid()
    r1 = tk.Radiobutton(app, text="Km<->Milla",variable=opcion, value=1)
    r1.grid()
    r2 = tk.Radiobutton(app, text="Celsius<->Fahrenheit",variable=opcion, value=2)
    r2.grid()
    def abrir_ventana():
        if opcion.get() == 1:
            app.destroy
            Km_Milla()
        elif opcion.get() == 1:
            app.destroy
            Celsius_Fahrenheit()
    boton = tk.Button(app, text="Seleciona", command=abrir_ventana)
    boton.grid()
    app.mainloop()

def Km_Milla():
    app = tk.Tk()
    app.geometry("500x500")
    app.title("Km<->Milla")
    explicacion1 = tk.Label(app, text="Escribir Kilometros")
    explicacion1.grid()
    entrada1 = tk.Entry(app)
    entrada1.grid()
    explicacion2 = tk.Label(app, text="Escribir Milla")
    explicacion2.grid()
    entrada2 = tk.Entry(app)
    entrada2.grid()
    def calcular():
        try: 
            if entrada1.get():
                valor = KmMilla(entrada1.get())
                resultado.set(f"{entrada1.get()} Kilometros son {valor:.2f} Milla")
            elif entrada2.get():
                valor = MillaKm(entrada2.get())
                resultado.set(f"{entrada2.get()} Milla son {valor:.2f} Kilometros")
            else:
                resultado.set(f"")
        except:
            resultado.set("Error: valor no valido")
    boton = tk.Button(app, text="Calcular", command=calcular)
    boton.grid()
    resultado = tk.StringVar()
    tk.Label(app, textvariable=resultado).grid()
    app.mainloop()

def Celsius_Fahrenheit():
    app = tk.Tk()
    app.geometry("500x500")
    app.title("Celsius<->Fahrenheit")
    explicacion1 = tk.Label(app, text="Escribir Celsius")
    explicacion1.grid()
    entrada1 = tk.Entry(app)
    entrada1.grid()
    explicacion2 = tk.Label(app, text="Escribir Fahrenheit")
    explicacion2.grid()
    entrada2 = tk.Entry(app)
    entrada2.grid()
    resultado = tk.StringVar()
    tk.Label(app, textvariable=resultado).grid()
    def calcular():
        try: 
            if entrada1.get():
                valor = Celfa(entrada1.get())
                resultado.set(f"{entrada1.get()} Celcius son {valor:.2f} Fahrenheit")
            elif entrada2.get():
                valor = Facel(entrada2.get())
                resultado.set(f"{entrada2.get()} Fahrenheit son {valor:.2f} Celsius")
            else:
                resultado.set(f"")
        except:
            resultado.set("Error: valor no valido")
    boton = tk.Button(app, text="Calcular", command=calcular)
    boton.grid()
    app.mainloop()
app1()