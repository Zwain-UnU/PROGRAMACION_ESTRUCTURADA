import funciones

pelis = {
    "Nombre": "toy story 5",
    "Duración": "120 minutos",
    "Idioma": "Español",
    "Clasificacion": "A",
    "Genero": "animada"
}

def menuPrincipal():
    print("\n\t\t...:::: M E N U  P R I N C I P A L ::::...\n")
    opcion = input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\
\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe una opcion: ").strip()
    return opcion


def agregarPeliculas(pelis):
    print("\n\t\t...:::: AGREGAR CARACTERISTICAS DE UNA PELICULA ::::...\n")
    caracteristica = input("Introducir el nombre de la caracteristica: ").title().strip()
    valor = input("Introducir el nombre del valor: ").upper().strip()
    pelis[caracteristica] = valor
    funciones.accionExitosa()


def mostrarPeliculas(pelis):
    print("\n\t\t...:::: MOSTRAR LAS CARACTERISTICAS DE LA PELICULA ::::...\n")
    if len(pelis) > 0:
        print("\tCaracteristica\t\tValor\n")

        for i in pelis:
            print(f"{i}\t\t{pelis[i]}")

        funciones.espereTecla()
    else:
        input("...¡No existe la pelicula que estas buscando, verifique!...")


def limpiarPeliculas(pelis):
    if len(pelis) > 0:
        opc = ""
        while opc != "si" and opc != "no":
            opc = input("¿Deseas limpiar la pelicula (Si/No)? ").lower().strip()

        if opc == "si":
            pelis.clear()
            funciones.accionExitosa()
    else:
        input("...¡No hay peliculas que borrar!...")


def buscarPeliculas(pelis):
    print("\n\t\t...:::: BUSCAR UNA CARACTERISTICA DE LA PELICULA ::::...\n")
    caracteristica = input("Escribir el nombre de la caracteristica: ").title().strip()

    noencontro = False

    for i in pelis:
        if caracteristica == i:
            print("\tCaracteristica\t\tValor\n")
            print(f"{i}\t\t{pelis[i]}")
            noencontro = True
            break

    if noencontro:
        funciones.espereTecla()
    else:
        input("...¡No existe la pelicula que estas buscando, verifique!...")


def borrarPeliculas(pelis):
    print("\n\t\t...:::: BORRAR UNA CARACTERISTICA DE LA PELICULA ::::...\n")
    caracteristica = input("Escribir el nombre de la caracteristica: ").title().strip()

    noencontro = False

    for i in pelis:
        if caracteristica == i:
            print("\tCaracteristica\t\tValor\n")
            print(f"{i}\t\t{pelis[i]}")
            noencontro = True

            opc = ""
            while opc != "si" and opc != "no":
                opc = input("¿Deseas borrar la pelicula (Si/No)? ").lower().strip()

            if opc == "si":
                pelis.pop(caracteristica)
                funciones.accionExitosa()

            break

    if not noencontro:
        input("...¡No existe la pelicula que estas buscando, verifique!...")


def modificarPeliculas(pelis):
    print("\n\t\t...:::: MODIFICAR EL VALOR DE LA CARACTERISTICA ::::...\n")
    caracteristica = input("Escribir el valor de la caracteristica: ").title().strip()

    noencontro = False

    for i in pelis:
        if caracteristica == i:
            print("\tCaracteristica\t\tValor\n")
            print(f"{i}\t\t{pelis[i]}")

            opc = ""
            while opc != "si" and opc != "no":
                opc = input("¿Deseas modificar el valor de la caracteristica de la pelicula (Si/No)? ").lower().strip()

            if opc == "si":
                pelis[caracteristica] = input(
                    "Escribe el valor de la caracteristica de la pelicula: "
                ).upper().strip()

                funciones.accionExitosa()

            noencontro = True
            break

    if not noencontro:
        input("...¡No existe la caracteristica que estas buscando, verifique!...")