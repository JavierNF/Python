# https://ellibrodepython.com/encapsulamiento-poo
#Característica de POO
#modificadores de acceso : private, public, protected ....
#ocultar atributos, métodos o clases al resto

#protected. Unicamente se puede usar en sus clases derivadas. hijas.

class Encapsular():
    nombre='clase encapsulada' #atributo sin nada. es público*
    __ciudad='sevilla' #atributo private. unicamente accesible en la clase
    def __secreto(self): #metodo de instancia privato. No accesible nada más que desde la clase
        print('mensaje secreto')
    def _paraHija(self): #método protected para que pueda usarse en la hija
        print('mensaje para hija')

class Hija(Encapsular): #herencia
    pass


encapsulamiento=Encapsular()
print(encapsulamiento.nombre)
#print(encapsulamiento.__ciudad) #no es accesible desde fuera de la clase
#encapsulamiento.secreto()

hija=Hija()
print(hija.nombre) #ok. porque la hija accede a una propiedad publica
#print(hija.ciudad) #error porque ciudad es private
#hija.secreto() #error porque secreto es private
hija._paraHija()

