# personas/main.py
from estudiante import Estudiante
from administrativo import Administrativo
from docente import Docente

# Creación de objetos de ejemplo
estudiante = Estudiante("Juan Pérez", 20, "Ingeniería")
administrativo = Administrativo("Ana López", 35, "Secretaria")
docente = Docente("Carlos Martínez", 40, "Matemáticas")

# Mostrando la información
print(estudiante.mostrar_informacion())
print(administrativo.mostrar_informacion())
print(docente.mostrar_informacion())
