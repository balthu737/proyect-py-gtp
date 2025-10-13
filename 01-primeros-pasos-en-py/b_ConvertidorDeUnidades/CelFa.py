#crea una funcion
def CelFa(celsiu):
    #variable que pide un numero y lo convierte en flotante 
    celsius = float(celsiu)
    #variable que hace calculo con la variable anterior
    fahrenheit = celsius *  9/5 + 32
    #retorna el resultado
    #return f'El resultado es: {fahrenheit}'
    return f"{celsius} Celcius son {fahrenheit:.2f} Fahrenheit"
#crea una funcion
def FaCel(fahr):
    #variable que pide un numero y lo convierte en flotante
    fahrenheit = float(input(fahr))
    #variable que hace calculo con la variable anterior
    celsius = (fahrenheit - 32) * 5/9
    #retorna el resultado
    #return f'El resultado es: {celsius}'
    return f"{fahrenheit} Fahrenheit son {celsius:.2f} Celsius"