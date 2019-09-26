#Acumulado.py
#Autor: Mirna Jackelyne Triana Sanchez
#Fecha: 18/09/2019

acumulado = int(0)
numero = str("")
#se inicializan las variables como vacias
while True:
    numero = input("Dame un numero entero: ")
    if numero == "":
        print("Vacio. salida del programa")
        break
#se indica que el programa dejara de cumplir con el ciclo cuando
#la cantidad capturada este vacia 
    else:
        acumulado += int(numero)
        salida = "Monto acumulado: {}"
        print(salida.format(acumulado))
#de lo contrario el ciclo se repetira y seguira acumulando (sumando)
#los valores capturados
