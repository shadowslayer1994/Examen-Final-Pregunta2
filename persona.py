from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def mostrar_informacion(self):
        pass
