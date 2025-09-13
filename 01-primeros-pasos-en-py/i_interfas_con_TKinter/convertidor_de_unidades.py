import tkinter as tk
from tkinter import messagebox

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
            Km_Milla()
        elif opcion.get() == 2:
            Celsius_Fahrenheit()
        elif opcion.get() == 0:
            messagebox.showwarning("atencion", "por favor selecione un opcion")
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
    resultado = tk.StringVar()
    txtlabel = tk.Label(app, textvariable=resultado)
    txtlabel.grid()
    def calcular():
        try: 
            if entrada1.get():
                km = float(entrada1.get())
                valor = km/1.609
                resultado.set(f"{entrada1.get()} Kilometros son {valor:.2f} Milla")
            elif entrada2.get():
                milla = float(entrada2.get())
                valor = milla*1.609
                resultado.set(f"{entrada2.get()} Milla son {valor:.2f} Kilometros")
            else:
                resultado.set(f"")
        except:
            resultado.set("Error: valor no valido")
    boton = tk.Button(app, text="Calcular", command=calcular)
    boton.grid()
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
    txtlabel = tk.Label(app, textvariable=resultado)
    txtlabel.grid()
    def calcular():
        try: 
            if entrada1.get():
                celsius = float(entrada1.get())
                valor = celsius*9.5+32
                resultado.set(f"{entrada1.get()} Celcius son {valor:.2f} Fahrenheit")
            elif entrada2.get():
                fahrenheit = float(entrada2.get())
                valor = (fahrenheit-32)*5/9
                resultado.set(f"{entrada2.get()} Fahrenheit son {valor:.2f} Celsius")
            else:
                resultado.set(f"")
        except:
            resultado.set("Error: valor no valido")
    boton = tk.Button(app, text="Calcular", command=calcular)
    boton.grid()
    app.mainloop()

