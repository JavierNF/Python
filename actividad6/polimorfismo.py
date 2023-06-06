# https://www.cosmiclearn.com/lang-es/python-polymorphism.php

# método. tiene una respuesta diferente en función del objeto que le llame
#sobrecarga de métodos : suele estar relacionado.

#metodo(argumento,argumento=None) : Python soporta argumentos con valores predeterminados
#Python No soporta sobrecarga como en otros lenguajes

#overload
def comer(quien,que,donde='en tu casa'): #ejemplo de sobrecarga *
    print(f'{quien} está comiendo {que} en {donde}')
#ejemplo de polimorfismo
comer('laura','chuletas')
comer('pepe','solomillo',' en un bar') #uso es como sobrecarga, pero Python NO la soporta estrictamente

#Polimorfismo en las clases
class Estudiante():
    def hacerExamen(self):
        print('el examen es teórico de 20 preguntas tipo test')

class GradoMedio(Estudiante):
    pass
class GradoSuperior(Estudiante):
    def hacerExamen(self): #sobreescritura
        print('el examen es práctica  y entrega PDF')
class DobleCiclo(Estudiante):
    def hacerExamen(self): #sobreescritura
        print('el examen es práctica  en ordinaria')

alumno1=GradoMedio()
alumno2=GradoSuperior()
alumno3=DobleCiclo()
alumno4=GradoSuperior()
alumno5=GradoMedio()

convocatoria=[alumno1,alumno2,alumno3,alumno4,alumno5]
for alumno in convocatoria:
    alumno.hacerExamen() #polimorfismo




