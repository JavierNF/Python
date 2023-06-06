# This is a sample Python script.
from datetime import datetime
import pandas as pd
import numpy as np
from pandas._config import dates


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def actividad10():
    nombre = input('dime tu nombre')
    fecha = input('dime la fecha a consultar dd-mm-yyyy')
    print(f'Tu nombre es {nombre} y la fecha a consultar es {fecha}')
    fechadate = datetime.strptime(fecha, '%d-%m-%Y')
    diadelmes = fechadate.day
    diadelasemana=fechadate.weekday()
    print(f'el  día del mes {diadelmes}')
    print(f'el  día de la semana es  {diadelasemana}')

    #añadir la condición

    if diadelmes in (5,9,14,22) and diadelasemana<5:
        print('toca natación')
    if diadelmes in (14,19,28) and diadelasemana<5:
        print('toca inglés')
    if diadelasemana==5:
        print('toca baloncesto')

def prueba():
#pide la ciudad de entrega
#si la ciudad es madrid, valencia o barcelona, el coste de envío de 5.99
#si es otra, el coste de envío es 7.99
#a toledo hay promoción especial. y el coste es 1.99
    ciudad=input('dime la ciudad de entrega: ')
    if ciudad.lower() in ('madrid', 'valencia', 'barcelona'):
        print('el coste de envío es 5.99')
    elif ciudad.lower()=='toledo':
        print('el coste de envío con promoción especial es 1.99')
    else:
        print('el coste general es 7.99')

def iterar():
    #pide el primer número
    #pide el segundo número
    #muestra los números que hay entre esos dos
    #si el segundo número es menor que el primero... que muestre un mensaje diciendo que no hay
    n1=int(input('dime un numero'))
    n2=int(input('dime un segundo numero'))
    if n1>n2:
        print('no hay numeros')
    else:
        for n in range(n1+1,n2):
            print(n)

def librerias():
    s=pd.Series([5, 9, 6, 7, 8])
    df = pd.DataFrame(np.random.randn(10, 6))
    print(s)
    print(df)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
#actividad10()
    #prueba()
    #iterar()
    librerias()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
