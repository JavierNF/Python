#matricula:idmatricula, fechamatricula, idalumno, idcurso : tabla de pedidos. tabla relaciional
#mostrar los datos de matrícula - método de la clase matricula
#reto*:método que muestra las mátriculas realizadas en mi centro
class Matricula: #PascalCase
    def __init__(self,id_matricula,fecha_matricula,alumno,curso):
        self.id_matricula=id_matricula #snake_case
        self.fecha_matricula=fecha_matricula
        self.alumno=alumno
        self.curso=curso
    def infoMatricula(self): #camelCase
        print(f'Info Matrícula : {self.id_matricula} alta {self.fecha_matricula} alumno {self.alumno}')