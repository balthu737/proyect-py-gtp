#llama a un archivo y a una funcion epecifica
from ConKmMilla import KmMilla
#llama a un archivo y a una funcion epecifica
from ConKmMilla import MillaKm
#llama a un archivo y a una funcion epecifica
from CelFa import CelFa
#llama a un archivo y a una funcion epecifica
from CelFa import FaCel
#variable que pide una peticion
pan = input("¿Qué queres calcular? Km<->Milla/Celsius<->Fahrenheit ")
#condicion que compara la varible con la peticion
if pan == "Km<->Milla":
    #variable que pide que calcular
    jabon = input("¿Qué queres calcular? Km->Milla/Milla->Km ")
    #condicion que compara que calculo hacer
    if jabon == "Km->Milla":
        #imprime una funcion
        print(KmMilla())
    #condicion que compara que calculo hacer
    elif jabon == "Milla->Km":
        #imprime una funcion
        print(MillaKm())
    #condicion cierra
    else :
        print("No se que queres decir flaco")
#condicion que compara la varible con la peticion
elif pan == "Celsius<->Fahrenheit":
    #variable que pide que calcular
    jabon = input("¿Qué queres calcular? Celsius->Fahrenheit/Fahrenheit->Celsius ")
    #condicion que compara que calculo hacer
    if jabon == "Celsius->Fahrenheit":
        #imprime una funcion
        print(CelFa())
    #condicion que compara que calculo hacer
    elif jabon == "Fahrenheit->Celsius":
        #imprime una funcion
        print(FaCel)
    #condicion cierra
    else :
        #imprime una funcion
        print("Que haces flaco??")
#condicion cierra
else :
    print("No te entendi")
