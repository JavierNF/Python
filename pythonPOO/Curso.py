#cursos:id,nombre, creditos, añosdeestudio - entidad - modelo - dataClass
#mostrar la ficha del curso - método de la curso
class Curso:
    def __init__(self,id,nombre,creditos,anno_estudio):
        self.id=id
        self.nombre=nombre
        self.creditos=creditos
        self.anno_estudio=anno_estudio
    def fichaCurso(self):
        print(f'Datos del curso {self.nombre} Creditos {self.creditos} en {self.anno_estudio} años')
