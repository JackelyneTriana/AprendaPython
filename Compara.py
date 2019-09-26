#Compara.py
#Autor: Mirna Jackelyne Triana Sanchez
#Fecha: 18/09/2019

numero1 = input("Numero 1: ")
numero2 = input("Numero 2: ")
salida = "Numeros proporciionados: {} y {}, {}"
#se piden 2 numeros y se realizan las siguientes comparaciones
if numero1 == numero2:
#si los numeros son iguales se cumple la anterior comparacion
    print(salida.format(numero1, numero2, "Los numeros son iguales"))
else:
    if numero1 > numero2:
    #de lo contrario entra en esta comparacion
        print(salida.format(numero1, numero2, "El primer numero es mayor"))
    else:
    #por ultimo si no cumple ninguna de las anteriores significa que
    #el numero 2 es el mayor
        print(salida.format(numero1, numero2, "El segundo numero es mayor"))
        
