#Conversion.py
#Autor: Mirna Jackelyne Triana Sanchez
#Fecha: 18/09/2019

numero="1234"
#al declarar el valor de la variable numero entre comillas automaticamente
#se toma como un valor de texto (str)
print(type(numero))
#imprime el tipo de dato de la variable (str)
numero=int(numero)
#se cambia el tipo de dato de la variable numero
print(type(numero))
#imprime el tipo de dato (int)
salida="El numero utilizado es {}"
print(salida.format(numero))
#se da salida al valor de la variable usando .format
