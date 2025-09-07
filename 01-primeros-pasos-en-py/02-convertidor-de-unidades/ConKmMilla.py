#crea una funcion
def KmMilla():
    #variable que pide un numero y lo convierte en flotante
    km = float(input("km= "))
    #variable que calcula con la variable anterior
    milla = km / 1.609
    #retorna el resultado
    return f'El resultado es: {milla}' 
#crea una funcion
def MillaKm():
    #variable que pide un numero y lo convierte en flotante
    milla = float(input("Milla= "))
    #variable que calcula con la variable anterior
    km = milla * 1.609
    #retorna el resultado
    return f'El resultado es: {km}' 
