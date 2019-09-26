#Tablas.py
#Autor: Mirna Jackelyne Triana Sanchez
#Fecha: 18/09/2019

for j in range(1,11):
#para cada elemento del rango 1 al 11 imprimir lo siguiente:
    encabezado = "Tabla del {}"
    print(encabezado.format(j))

    for i in range(1,11):
    #para cada elemento del rango 1 al 11 imprimir lo siguiente:
        salida = "{} x {} = {}"
        print(salida.format(i, j, i*j))
    #ya que este ciclo for se encuentra dentro del ciclo anterior
    #permite utilizar los valores de este
    else:
        print()
