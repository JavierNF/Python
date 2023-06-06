#1. Crea una lista con 6 ciudades.
#Muestra las ciudades por consola. 
# #En mayúsculas y al lado el número de letras que tiene.
#solución : Lista []
ciudades=['madrid','sevilla','valencia','almería','córdoba','granada','almería'] #soporta repetición
for ciudad in ciudades:
    print(f'la ciudad es {ciudad.upper()} - {len(ciudad)}')

#2. Crea una colección con 5 marcas de coche. 
#Muestra el listado de ordenado en orden descendente.
#solución : lista
coches=['seat','renault','bmw','audi','mercedes']
coches.sort() #lista soporta orden
coches.reverse() #orden descendente
for coche in coches:
    print(coche)

#3. Crea una colección con 5 clientes y su facturación anual en euros.
#Muestra el total de facturación y la facturación media. #acumulador
#solución : diccionario
clientes={'iberdrola':15000,'endesa':14800,'naturgy':36524,'enagas':14785,'fluidra':95265}
total=0
for v in clientes.values():
    total=total+v #acumulador
print(f'El total de facturacion es {total}')
print(f'El promedio de facturación es {total/len(clientes)}')

#4. Por consola te pide un número hasta que pulses 0.
#Muestra la suma total de estos números.
numero=1
suma=0 #totalizador
while numero!=0:
    numero=int(input('dime un numero')) #convertir a int
    suma=suma+numero
    #suma+=numero
print(f'El total es {suma}') #se ejecuta cuando sales del bucle

#5. En una colección introduce los precios de 6 artículos. 
# No necesitamos los nombres de los artículos.
#Muestra el precio promedio. 
# Si es superior a 5, indica que debemos bajar el precio un 5%
#solucion : lista
precios=[12.95,35.96,74.58,65.25,14.65] #lista
totalPrecio=0 #acumulador
for precio in precios:
    totalPrecio+=precio #incremento
print(f'El precio medio es {totalPrecio/len(precios)}')
if totalPrecio/len(precios)>5:
    print('debemos bajar el precio un 5 %')

