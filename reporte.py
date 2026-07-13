import csv

# Sistema de Control de Entrada - Eventos VIP
asistentes = []
cupo_maximo = 20

while True:

    print("\n--- EVENTO VIP ---")
    print("1. Registrar persona")
    print("2. Ver lista")
    print("3. Editar nombre")
    print("4. Eliminar persona")
    print("5. Ver estadísticas")
    print("6. Generar reporte")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        if len(asistentes) >= cupo_maximo:
            print("No hay más cupos disponibles.")

        else:
            nombre = input("Ingrese el nombre: ")

            if nombre in asistentes:
                print("Esa persona ya está registrada.")
            else:
                asistentes.append(nombre)
                print("Persona registrada correctamente.")

    elif opcion == "2":

        if len(asistentes) == 0:
            print("No hay personas registradas.")

        else:
            print("\nLista de asistentes:")

            for i in range(len(asistentes)):
                print(i, "-", asistentes[i])

    elif opcion == "3":

        if len(asistentes) == 0:
            print("No hay personas registradas.")

        else:
            try:
                indice = int(input("Ingrese el número de la persona a editar: "))

                if indice >= 0 and indice < len(asistentes):

                    nuevo_nombre = input("Ingrese el nuevo nombre: ")

                    if nuevo_nombre in asistentes:
                        print("Ese nombre ya existe.")

                    else:
                        asistentes[indice] = nuevo_nombre
                        print("Nombre actualizado correctamente.")

                else:
                    print("Índice no válido.")

            except ValueError:
                print("Error. Debe ingresar un número.")

    elif opcion == "4":

        if len(asistentes) == 0:
            print("No hay personas registradas.")

        else:
            try:
                indice = int(input("Ingrese el número de la persona a eliminar: "))

                if indice >= 0 and indice < len(asistentes):

                    eliminado = asistentes.pop(indice)
                    print("Se eliminó a:", eliminado)

                else:
                    print("Índice no válido.")

            except ValueError:
                print("Error. Debe ingresar un número.")

    elif opcion == "5":

        print("\n--- ESTADÍSTICAS ---")
        print("Personas registradas:", len(asistentes))
        print("Cupos disponibles:", cupo_maximo - len(asistentes))

    elif opcion == "6":

        if len(asistentes) == 0:
            print("No hay asistentes registrados para generar el reporte.")

        else:
            try:
                with open("reporte_asistentes.csv", "w", newline="", encoding="utf-8") as archivo:

                    escritor = csv.writer(archivo)
                    escritor.writerow(["Número", "Nombre"])

                    for i in range(len(asistentes)):
                        escritor.writerow([i + 1, asistentes[i]])

                print("Reporte generado correctamente.")
                print("Archivo creado: reporte_asistentes.csv")

            except Exception as e:
                print("Error al generar el reporte:", e)

    elif opcion == "7":

        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")