def age():
    AñoNacimiento = input("¿Cual es tu año de nacimiento? ")
    AñoActual = input("¿Cual es el año actual? ")
    age1 = int(AñoNacimiento)
    age2 = int(AñoActual)
    Age = age2-age1
    return f'tu edad es: {Age}'