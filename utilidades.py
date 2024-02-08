def mostrar_tabla_posiciones_cuadrangular(equipos_cuadrangular):
    equipos_cuadrangular.sort(key=lambda x: x.puntos_cuadrangular_1, reverse=True)
    print("Tabla de Posiciones Cuadrangular 1:")
    print("{:<20} {:<10}".format("Equipo", "Puntos"))
    for equipo in equipos_cuadrangular:
        if equipo.puntos_cuadrangular_1 != 0:
            print("{:<20} {:<10}".format(equipo.nombre, equipo.puntos_cuadrangular_1))
        print()

    equipos_cuadrangular.sort(key=lambda x: x.puntos_cuadrangular_2, reverse=True)
    print("Tabla de Posiciones Cuadrangular 2:")
    print("{:<20} {:<10}".format("Equipo", "Puntos"))
    for equipo in equipos_cuadrangular:
        if equipo.puntos_cuadrangular_2 != 0:
            print("{:<20} {:<10}".format(equipo.nombre, equipo.puntos_cuadrangular_2))
        print()

def mostrar_cuadrangulares(cuadrangular_1, cuadrangular_2):
    print("Cuadrangular 1:")
    for equipo in cuadrangular_1:
        print("- " + equipo.nombre)
    
    print("\nCuadrangular 2:")
    for equipo in cuadrangular_2:
        print("- " + equipo.nombre)
    print()

def mostrar_tabla_posiciones(equipos_cuadrangular_1, equipos_cuadrangular_2):
    equipos = equipos_cuadrangular_1 + equipos_cuadrangular_2
    equipos.sort(key=lambda x: x.puntos_cuadrangular_1 + x.puntos_cuadrangular_2, reverse=True)
    
    print("Tabla de Posiciones:")
    print("{:<20} {:<10}".format("Equipo", "Puntos"))
    for equipo in equipos:
        puntos_totales = equipo.puntos_cuadrangular_1 + equipo.puntos_cuadrangular_2
        print("{:<20} {:<10}".format(equipo.nombre, puntos_totales))
    print()
