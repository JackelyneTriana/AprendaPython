opcion_elegida = input("Elige la opcion que entre A, B o C: ")

while opcion_elegida:
    if opcion_elegida == "A":
        print("Seleccionaste A")
        opcion_elegida = ""
    elif opcion_elegida == "B":
        print("Seleccionaste B")
        opcion_elegida = ""
    elif opcion_elegida == "C":
        print("Seleccionaste C")
        opcion_elegida = ""
    else:
        opcion_elegida = input("Opcion incorrecta, intenta nuevamente: ")
