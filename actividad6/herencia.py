# https://ellibrodepython.com/herencia-en-python
#Característica de POO. Python la soporta.
#sobreescritura : override : Característica en la herencia

#clase Padre, base, superclase
class Padre:
    nombre='maría pérez' #atributo
    def __init__(self,nombre,ciudad) -> None:
        self.nombre=nombre
        self.ciudad=ciudad
    @staticmethod
    def saludar(): #metodo
        print('estoy saludando')
class Madre:
    unidades=15

#clase derivada, hija, subclase
class Hija(Padre,Madre): #heredar
    def __init__(self, nombre, ciudad) -> None:
        self.nombre=nombre
        self.ciudad=ciudad
        super().__init__(nombre, ciudad)
        
    #override - sobreescribir método
    @staticmethod
    def saludar(): #metodo estático. método instancia si tiene self
        print('estoy saludando desde la hija')

#instanciar las clases : Crea un objeto de esa clase en memoria
hija=Hija('marta sánchez','segovia') #instanciar
hija.saludar()
print(hija.nombre)
print(hija.unidades)

