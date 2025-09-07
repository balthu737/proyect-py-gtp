#crea una funcion
def CelFa():
    #variable que pide un numero y lo convierte en flotante 
    celsius = float(input("Celsius= "))
    #variable que hace calculo con la variable anterior
    fahrenheit = celsius *  9/5 + 32
    #retorna el resultado
    return f'El resultado es: {fahrenheit}'
#crea una funcion
def FaCel():
    #variable que pide un numero y lo convierte en flotante
    fahrenheit = float(input("Fahrenheit= "))
    #variable que hace calculo con la variable anterior
    celsius = (fahrenheit - 32) * 5/9
    #retorna el resultado
    return f'El resultado es: {celsius}'