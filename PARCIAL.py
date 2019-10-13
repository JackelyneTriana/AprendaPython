import statistics as stats

datos = []
suma = 0
contador = 0

while contador < 10:
    dato = input("Teclea un dato numerico entero: ")
    #if dato.isspace():
    #    print("Debes teclear un dato.")
    if (dato.isdigit() and dato.find(".")):
        dato = int(dato)
        datos.append(dato)
        suma = suma + dato
        contador = contador + 1
    else:
        print("El dato que ingresaste no es un dato numerico entero")

promedio = suma / 10
desv_est = stats.stdev(datos)
precio_min = promedio - desv_est
precio_max = promedio + desv_est

print("El precio maximo es {}, el precio minimo es {}".format(round(precio_max, 2), round(precio_min,2)))