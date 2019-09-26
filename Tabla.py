#Tabla.py
#Autor: Mirna Jackelyne Triana Sanchez
#Fecha: 18/09/2019

numero = input("Teclea un numero del 1 al 9: ")
#se pide un numero
numero = int(numero)
#se convierte el tipo de dato de str a int
for i in range(1,11):
#para cada elemento en un rango entre 1 y 11 hacer
#solo se tomara del 1 al 10
    salida = "{} x {} = {}"
    print(salida.format(numero, i, numero*i))
#imprime el dato a multiplicar, el elemeto en turno
#y la multiplicacion del numero por el elemento
