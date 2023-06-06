#POO. entidad, clase, Cliente
#python es un lenguaje indentado
class Cliente: #nomenculatura es PascalCase
    #constructor pide los atributos, campos, propiedades
    def __init__(self,id,nombre,email,pais,descuento):
        self.id=id #Any quiere decir cualquier tipo de dato. Python infiere el tipado de dato. No es un tipado fuerte como Java
        self.nombre_cliente=nombre #nomenclatura snake_case
        self.email=email
        self.pais=pais
        self.descuento=descuento
    #métodos
    #nomenclatura camelCase
    def info_Cliente(self):#método de instancia permite usar atributos de clase. self
        print(f'El cliente se llama {self.nombre_cliente}') #formato

