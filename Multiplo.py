#Multiplo.py
#Autor: Mirna Jackelyne Triana Sanchez
#Fecha: 18/09/2019

numero = int(input("Teclea un nuero entero: "))
multiplo3 = ((numero%3)==0)
multiplo5 = ((numero%5)==0)
multiplo7 = ((numero%7)==0)
#se evalua que el residuo de la division de el numero tecleado
#entre 3, 5 y 7 sea 0 para comprobar si es multiplo de alguno de
#los 3 numros
if ((multiplo3 and multiplo5) or multiplo7):
#se evalua si el numero es multiplo de 3 y 5 o de 7
#si cumple con alguna de las condiciones es correcto
    print("Correcto")
else:
    print("Incorrecto")
