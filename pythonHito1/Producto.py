class Producto:
    def __init__(self,id,nombre,unidades,precio,fecha_alta):
        self.id=id
        self.nombre=nombre
        self.unidades=unidades
        self.precio=precio #number, entero o decimales
        self.fecha_alta=fecha_alta #fecha : utilizar clase datetime
    def fichaProducto(self):
        print(f'los datos del producto son {self.nombre}')
