class Pedidos:
    def __init__(self,id_factura,fecha_factura,cliente,producto):
        self.id_factura=id_factura
        self.fecha_factura=fecha_factura
        self.cliente=cliente #pasar un number o un objeto
        self.producto=producto

    def infoPedido(self):
        print(f'Detalles de pedido {self.id_factura} - {self.fecha_factura}  - {self.cliente} - {self.producto}')

    def addDeseos(self):
        print('producto añadido a la lista de deseos')

    def finalizarCompra(self):
        print('compra finalizada')

    def pagoCompra(self):
        print('pasarela de pago para pagar')

    def facturaPDF(self):
        print('factura enviada en pdf')

    def seguimiento(self):
        print('sms enviado al cliente')