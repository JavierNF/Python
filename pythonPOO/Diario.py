from datetime import datetime

from Alumno import Alumno
from Curso import Curso
from Matricula import Matricula

#Alumno se registra. Actor alumno. método. constructor Alumno
#instancia de la clase Alumno : objeto
alumno1=Alumno(1,'juan','juan@gmail.com')
alumno2=Alumno(2,'laura','laura@gmail.com')

#crear cursos. Actor MEH metodo. constructor Curso
curso1=Curso(1,'dam1',120,2)
curso2=Curso(2,'c2',240,5)

#juan se quiere matricular en DAM1
matricula1=Matricula(100,datetime.now(),alumno1.nombre,curso1)
matricula2=Matricula(200,datetime.now(),alumno1.nombre,curso2)
matricula3=Matricula(300,'01/03/2022',alumno2.nombre,curso1)
matricula4=Matricula(400,'30/02/2022',alumno1.nombre,curso2)
#matricula1.infoMatricula()

#reto : almacenar los objetos de matricula en una collection : list, set, dict, tupla....
matriculaGetafe=[matricula1,matricula2,matricula3,matricula4] #almacenas
#las matriculas como objetos en un list

#dime los nombres y las fechas los alumnos matriculados
for matricula in matriculaGetafe:
    matricula.infoMatricula()





