#Aleatorio.py
#Autor: Mirna Jackelyne Triana Sanchez
#Fecha 18/09/2019

import random
#se importa la libreria random
numero1=float(10.5)
#se le da un valor fijo a la variable numero1 de tipo decimal(float)
def mifuncion():
#se define la funcion y su nombre
    numero2=float(random.randrange(1,10))
#se le da un valor aleatorio a la variable numero2
#se expresa que el valor de la variable solo puede estar en
#un rango entre 1 y 10
    mensaje="La suma de {} y {} es {}"
#se le da un valor a la variable mensaje haciendo espacio para
#los respectivos valores
    print(mensaje.format(numero1, numero2, numero1 + numero2))
#se imprime la variable mensaje (hacienddo la suma de las 2 variables
#en el tercer valor)
mifuncion()
#se manda a llamar a la funcion para que se ejecute todo
#lo que hay dentro de ella
