#Crear una clase Cliente con las propiedades, nombre, ciudad y facturacion en constructor.
#Alta al cliente : indra, madrid, 15000 / repsol, sevilla, 20000
#crea un método para mostrar los datos de los clientes

from random import random


class Cliente():
    def __init__(self,n,c,f) -> None:
        self.nombre=n
        self.ciudad=c
        self.facturacion=f
    def verDetalle(self):
        print(f'El cliente {self.nombre}, de la ciudad {self.ciudad} ha facturado {self.facturacion} euros')
    def totalFactura(self):
        if self.facturacion>50000:
            self.facturacion=self.facturacion*0.95
        total=self.facturacion*1.21
        print(f'El total de factura es {total} euros')
    def setFacturacion(self,facturacion): #ejemplo de setter
        self.facturacion=facturacion

cliente1=Cliente('indra','madrid',15000)
cliente2=Cliente('repsol','sevilla',20000)
cliente1.verDetalle()
cliente2.verDetalle()

#prepara un método en la clase Cliente para calcular el totalFactura
#facturacion + 21% iva. Si la facturación es superior a 50.000 tiene un descuento
#antes de iva del 5%

#muestra el total de facturación para cada cliente.
#tenemos un nuevo cliente : Iberia, Sevilla, 65000 ¿cuánto es su totalFactura?
cliente1.totalFactura()
cliente2.totalFactura()
cliente3=Cliente('iberia','sevilla',65000)
cliente3.totalFactura()

#crea un método para cambiar la facturación del cliente (ejemplo de setter)
#el nuevo método pide como parámetro la nueva facturación. 
#llama al método verDetalle y comprueba que la facturación se ha actualizado.
cliente1.setFacturacion(54000)
cliente1.verDetalle()

#necesitamos crear 10 clientes nuevos
#nombre y la ciudad, cliente100, cliente101 ....y la ciudad madrid
#la facturación será un número aleatorio entre 1000 y 50000
#muestra el detalle de los 10 nuevos clientes

clientes=[] #lista para almacenar los clientes creados
for i in range(11): #bucle hasta 10
    if i>=10: #para pintar cliente1xx
        cliente=Cliente(f'cliente1{i}','madrid',round(50000*random(),2))
    else:
        cliente=Cliente(f'cliente10{i}','madrid',round(50000*random(),2)) #aleatorio
    clientes.append(cliente)

for c in clientes: #recorre los clientes de la lista
    c.verDetalle();

    