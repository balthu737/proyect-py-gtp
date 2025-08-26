from ConKmMilla import KmMilla
from ConKmMilla import MillaKm
from CelFa import CelFa
from CelFa import FaCel

pan = input("¿Qué queres calcular? Km<->Milla/Celsius<->Fahrenheit ")
if pan == "Km<->Milla":
    jabon = input("¿Qué queres calcular? Km->Milla/Milla->Km ")
    if jabon == "Km->Milla":
        print(KmMilla())
    elif jabon == "Milla->Km":
        print(MillaKm())
    else :
        print("No se que queres decir flaco")
elif pan == "Celsius<->Fahrenheit":
    jabon = input("¿Qué queres calcular? Celsius->Fahrenheit/Fahrenheit->Celsius ")
    if jabon == "Celsius->Fahrenheit":
        print(CelFa())
    elif jabon == "Fahrenheit->Celsius":
        print(FaCel)
    else :
        print("Que haces flaco??")
else :
    print("No te entendi")
