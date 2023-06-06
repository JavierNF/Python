#alumno:id, nombre, email
class Alumno:
    def __init__(self,id,nombre,email):
        self.id=id
        self.nombre=nombre
        self.email=email
    def fichaAlumno(self):
        print(f'Datos de alumno {self.nombre}')