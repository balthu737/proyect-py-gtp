#creamos una funcion que hace un calculo con la edad 
def age():
    #variable con un input que pide la edad 
    AñoNacimiento = input("¿Cual es tu año de nacimiento? ")
    #variable con un imput que pide el año
    AñoActual = input("¿Cual es el año actual? ")
    #convierte la varible 1 en un numero entero
    age1 = int(AñoNacimiento)
    #convierte la variable 2 en un numero entero
    age2 = int(AñoActual)
    #busca la edad del sujeto
    Age = age2-age1
    #devuelve la edad
    return f'tu edad es: {Age}'