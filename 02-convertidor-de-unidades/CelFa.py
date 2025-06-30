def CelFa():
    celsius = float(input("Celsius= "))
    fahrenheit = celsius *  9/5 + 32
    return f'El resultado es: {fahrenheit}'

def FaCel():
    fahrenheit = float(input("Fahrenheit= "))
    celsius = (fahrenheit - 32) * 5/9
    return f'El resultado es: {celsius}'