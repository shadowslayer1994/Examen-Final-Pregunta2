from persona import Persona

class Administrativo(Persona):
    def __init__(self, nombre, edad, puesto):
        self.nombre = nombre
        self.edad = edad
        self.puesto = puesto

    def mostrar_informacion(self):
        return f"Administrativo: {self.nombre}, Edad: {self.edad}, Puesto: {self.puesto}"
