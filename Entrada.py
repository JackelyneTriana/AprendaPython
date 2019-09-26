#Entrada.py
#Autor: Mirna Jackelyne Triana Sanchez
#Fecha: 18/09/2019

print("Teclea un numero entero")
entrada=input()
#le asigna a la variable entrada el valor que teclee el usuario
print(type(entrada))
#se imprime el tipo de dato de la variable (str)
Entero=(entrada.isdigit() and entrada.find(".")==-1)
#se comprueba que el dato ingresado sea un digito
#con la extension find se busca un punto en el valor de la entrada
#si este retorna el valor -1 (significa que no se encontro un punto)
#la variable Entero es cierta(true)
if(Entero):
    print("El dato es entero")
else:
    print("El dato no es entero, intenta otra ves")
#de lo contrario la variable es falsa
