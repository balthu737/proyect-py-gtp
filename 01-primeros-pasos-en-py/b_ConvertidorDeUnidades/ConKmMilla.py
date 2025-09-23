#crea una funcion
def KmMilla(KM):
    #variable que pide un numero y lo convierte en flotante
    km = float(KM)
    #variable que calcula con la variable anterior
    milla = km / 1.609
    #retorna el resultado
    #return f'El resultado es: {milla}' 
    return milla
#crea una funcion
def MillaKm(MILLA):
    #variable que pide un numero y lo convierte en flotante
    milla = float(MILLA)
    #variable que calcula con la variable anterior
    km = milla * 1.609
    #retorna el resultado
    #return f'El resultado es: {km}' 
    return km
