from cantidad_de import separar_y_contar
from cantidad_de_lineas import cantidad_de_lineas
from cantidad_de_palabras import cantidad_de_palabras
from top5 import top5
while True:
    print("""Hola bienvenido a analizador de textos
1) Cantidad de lineas
2) Cantidad de palabras
3) Todas las palabras usadas de mayor a menor
4) Top 5 palabras mas usadas
5) Salir""")
    eleccion = int(input("Elegi uno: "))
    if eleccion == 1:
        ruta = input("Cual es la ruta absoluta del archivo txt para analizar: ")
        print(cantidad_de_lineas(ruta))
    elif eleccion == 2:
        ruta = input("Cual es la ruta absoluta del archivo txt para analizar: ")
        print(cantidad_de_palabras(ruta))
    elif eleccion == 3:
        ruta = input("Cual es la ruta absoluta del archivo txt para analizar: ")
        print(separar_y_contar(ruta))
    elif eleccion == 4:
        ruta = input("Cual es la ruta absoluta del archivo txt para analizar: ")
        print(top5(ruta))
    elif eleccion == 5:
        break
    else:
        print("No contemplamos esa funcion")
