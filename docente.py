from persona import Persona

class Docente(Persona):
    def __init__(self, nombre, edad, asignatura):
        self.nombre = nombre
        self.edad = edad
        self.asignatura = asignatura

    def mostrar_informacion(self):
        return f"Docente: {self.nombre}, Edad: {self.edad}, Asignatura: {self.asignatura}"
