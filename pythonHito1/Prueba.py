from datetime import datetime

from Cliente import Cliente
from Pedidos import Pedidos
from Producto import Producto


def registrar_cliente():
    cliente1=Cliente(1,'juan','juan@gmail.com','francia',True)
    cliente1.info_Cliente()

def registrar_producto():
    producto1=Producto(10,'camisa',15,9.95,datetime.now())
    producto1.fichaProducto()

def registrar_pedido():
    cliente100=Cliente(100,'maria','maria@gmail.com','italia',False)
    producto100=Producto(100,'bufanda',5,9.95,datetime.now())

    #pedido1=Pedidos(100,datetime.now(),1,2) #Python tipado dinámico. cliente es un number... ok
    pedido2=Pedidos(101,datetime.now(),cliente100.nombre_cliente,producto100.nombre) #cliente es un objeto..ok
    pedido2.infoPedido()
    pedido2.addDeseos()
    pedido2.finalizarCompra()
    pedido2.pagoCompra()
    pedido2.facturaPDF()
    pedido2.seguimiento()

registrar_cliente()
registrar_producto()
registrar_pedido()