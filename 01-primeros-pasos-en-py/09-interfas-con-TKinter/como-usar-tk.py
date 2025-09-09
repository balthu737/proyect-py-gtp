#
import tkinter as tk
#
app = tk.Tk()
#
app.geometry("1000x1000")
#
app.configure(background="black")
#
app.title("Primera app")
#
texto = tk.Label(app, text="Hola")
texto.pack(fill=tk.BOTH, expand=True)
#
boton = tk.Button(app, text="click me", font=("Courire", 14), bg="#008a8e", fg="white")
boton.pack(fill=tk.BOTH, expand=True)
entrada = tk.Entry(app)
entrada.pack(fill=tk.BOTH, expand=True)
#
opcion = tk.Checkbutton(app, text="acepto los terminos")
opcion.pack(fill=tk.BOTH, expand=True)
#
r1 = tk.Radiobutton(app, text="opcion 1", value=1)
r1.pack(fill=tk.BOTH, expand=True)
#
r2 = tk.Radiobutton(app, text="opcion 2", value=2)
r2.pack(fill=tk.BOTH, expand=True)
#
lista = tk.Listbox(app)
#
lista.insert(1,"py")
lista.insert(2,"java")
lista.insert(3,"js")
lista.insert(4,"C++")
lista.pack(fill=tk.BOTH, expand=True)
#
#slider = tk.scale(app, from_=0, to=100, orient="horizontal")
#slider.pack(fill=tk.BOTH, expand=True)
#
spin = tk.Spinbox(app, from_=0, to=10)
spin.pack(fill=tk.BOTH, expand=True)
#
text = tk.Text(app, height=5, width=30)
text.pack(fill=tk.BOTH, expand=True)

app.mainloop()
