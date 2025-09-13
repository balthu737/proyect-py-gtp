import tkinter as tk

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
                resultado.set(f"")
            elif entrada2.get():
                resultado.set(f"")
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
    def calcular():
        try: 
            if entrada1.get():
                resultado.set(f"")
            elif entrada2.get():
                resultado.set(f"")
            else:
                resultado.set(f"")
        except:
            resultado.set("Error: valor no valido")
    boton = tk.Button(app, text="Calcular", command=calcular)
    boton.grid()
    resultado = tk.StringVar()
    tk.Label(app, textvariable=resultado).grid()
    app.mainloop()
app1()