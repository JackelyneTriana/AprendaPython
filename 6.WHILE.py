repeticiones = int(input("Cuantos nombres deseas escribir? "))
nombres = []
contador = 1
nombre = ""

while contador <= repeticiones:
    nombre = str(input("Escribe un nombre: "))
    nombres.append(nombre)
    contador = contador + 1

print("\nLa lista de los nombres que ingresaste: ")
for x in nombres: 
    print(x)
