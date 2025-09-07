#importamos TKinter y lo renombremos tk
import tkinter as tk
#creamos el objeto app (la ventana)
app = tk.Tk()
#le damos un tamaño a la ventana
app.geometry("500x500")
#le damos un color de fondo (por defecto es blanco)
app.configure(background="black")
#accedemos a la clase a windows manajer al titulo y renombremos el titulo de la clase
tk.Wm.wm_title(app, "app")
#llamamos al atributo de la instancia de la clase
app.mainloop()