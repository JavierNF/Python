#En Pycharm, crea una clase llamada Asignaturas.
#Esta clase almacena asignaturas con los atributos :
#código, nombre, créditos, grado
#en python NO es necesario definir el tipo de datos al declarar la variable

#Guarda todas las asignaturas en una colección a  tu gusto.
#Muestra las asignaturas ordenadas por créditos de mayor a menor usando un bucle.
#Muestra el total de créditos del total de asignaturas.

class Asignaturas:
    def __init__(self, codigo, nombre, creditos, grado): #constructor
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.grado = grado

    def fichaAsignaturas(self):
        print(f'los nombres y codigos de las asignaturas son {self.nombre} - {self.codigo}')

#crear objetos. Instanciar la clase Asignaturas
asignatura1=Asignaturas(100,'programación',120,'dam')
asignatura2=Asignaturas(200,'despliegue',80,'daw')
asignatura3=Asignaturas(300,'desarrollo web',110,'daw')
asignatura4=Asignaturas(400,'base de datos',95,'dam')

#collections: grupo de objetos, números, strings, fechas..
#se ordenan, permite repitir, mutable vs inmutable
#list : []
#set :{}
#dictiionari {key:value}

#list
asignaturas=[asignatura1,asignatura2,asignatura3,asignatura4]
#lista_ordenada=sorted(asignaturas)
for asignatura in asignaturas:
    print(asignatura.nombre)
    print(asignatura.creditos)

#dictionario
asignaturas_diccionario={asignatura1.nombre:asignatura1.creditos,asignatura2.nombre:asignatura2.creditos,asignatura3.nombre:asignatura3.creditos,asignatura4.nombre:asignatura4.creditos}
asignaturas_ordenadas=sorted(asignaturas_diccionario.items(),key=lambda x: x[1],reverse=True)
for a in asignaturas_ordenadas:
    print(a)

#total de créditos
total=sum(asignaturas_diccionario.values()) #programación funcional
print(f'el total de créditos es {total}')