class Persona:
    def __init__(self, nombre, año_de_nacimiento):
        self._nombre = nombre
        self._año_de_nacimiento = año_de_nacimiento
    def __str__(self):
        return f"Persona: {self._nombre}, nacido en {self._año_de_nacimiento}"
    def calcular_edad(self):
        año_actual = int(input("Que año es?: "))
        edad = año_actual- self.año_de_nacimiento
        return edad 
    def presentacion(self):
        edad = self.calcular_edad()
        print(f'hola soy {self.nombre} y tengo {edad}')
nombre = input("Cual es tu nombre?: ")
edad = int(input("Cual estu edad?: "))
persona = Persona(nombre, edad)
#persona.presentacion()
#print(persona)