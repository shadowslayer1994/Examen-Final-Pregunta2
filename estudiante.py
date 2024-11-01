from persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def mostrar_informacion(self):
        return f"Estudiante: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}"
