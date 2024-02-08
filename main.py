from equipo import Equipo
from partido import Partido
from utilidades import mostrar_tabla_posiciones_cuadrangular, mostrar_cuadrangulares, mostrar_tabla_posiciones
from db import EquipoDB
def main():
    equipos_db = EquipoDB()
    equipos = []
    partidos = []

    # Registra los equipos
    for i in range(1, 9):
        nombre_equipo = input(f"Ingrese el nombre del equipo {i}: ")
        equipos.append(Equipo(nombre_equipo))

    # Sorteo para los cuadrangulares
    import random
    random.shuffle(equipos)
    cuadrangular_1 = equipos[:4]
    cuadrangular_2 = equipos[4:]

    equipos = equipos_db.obtener_equipos()
    equipos_db.crear_equipo("Nuevo Equipo")
    equipos_nuevos = equipos_db.obtener_equipos()
    print("Equipos después de agregar uno nuevo:")
    for equipo in equipos_nuevos:
        print(equipo.nombre)

        # Muestra los cuadrangulares
    mostrar_cuadrangulares(cuadrangular_1, cuadrangular_2)

    # Registra los partidos para cada cuadrangular
    for equipo1 in cuadrangular_1:
        for equipo2 in cuadrangular_1:
            if equipo1 != equipo2:
                # Verifica si el partido ya ha sido registrado en sentido contrario
                partido_ya_registrado = any(partido.equipo1 == equipo2 and partido.equipo2 == equipo1 for partido in partidos)
                if not partido_ya_registrado:
                    partidos.append(Partido(equipo1, equipo2))

    for equipo1 in cuadrangular_2:
        for equipo2 in cuadrangular_2:
            if equipo1 != equipo2:
                # Verifica si el partido ya ha sido registrado en sentido contrario
                partido_ya_registrado = any(partido.equipo1 == equipo2 and partido.equipo2 == equipo1 for partido in partidos)
                if not partido_ya_registrado:
                    partidos.append(Partido(equipo1, equipo2))
    
    # Simula los partidos y actualiza los puntos
    for partido in partidos: 
        # Pide el marcador para el partido
        marcador = input(f"Ingrese el marcador para {partido.equipo1.nombre} vs {partido.equipo2.nombre} (separador por un -'): ")
        marcador_equipo1, marcador_equipo2 = map(int, marcador.split('-'))

        # Actualiza los puntos según el marcador
        if marcador_equipo1 > marcador_equipo2:
            partido.equipo1.puntos_cuadrangular_1 += 3 if partido.equipo1 in cuadrangular_1 else 0
            partido.equipo1.puntos_cuadrangular_2 += 3 if partido.equipo1 in cuadrangular_2 else 0
        elif marcador_equipo1 < marcador_equipo2:
            partido.equipo2.puntos_cuadrangular_1 += 3 if partido.equipo2 in cuadrangular_1 else 0
            partido.equipo2.puntos_cuadrangular_2 += 3 if partido.equipo2 in cuadrangular_2 else 0
        else:
            partido.equipo1.puntos_cuadrangular_1 += 1 if partido.equipo1 in cuadrangular_1 else 0
            partido.equipo1.puntos_cuadrangular_2 += 1 if partido.equipo1 in cuadrangular_2 else 0
            partido.equipo2.puntos_cuadrangular_1 += 1 if partido.equipo2 in cuadrangular_1 else 0
            partido.equipo2.puntos_cuadrangular_2 += 1 if partido.equipo2 in cuadrangular_2 else 0

    # Muestra la tabla de posiciones final
    mostrar_tabla_posiciones_cuadrangular(equipos)
    
    # Seleccionar los dos equipos con mayor cantidad de puntos de cada cuadrangular
    cuadrangular_1_top = sorted(cuadrangular_1, key=lambda x: x.puntos_cuadrangular_1, reverse=True)[:2]
    cuadrangular_2_top = sorted(cuadrangular_2, key=lambda x: x.puntos_cuadrangular_2, reverse=True)[:2]

    # Hacer un partido entre los dos equipos con mayor cantidad de puntos de cada cuadrangular
    partido_final_1 = Partido(cuadrangular_1_top[0], cuadrangular_1_top[1])
    partido_final_2 = Partido(cuadrangular_2_top[0], cuadrangular_2_top[1])

    # Simular los partidos de la final 1
    marcador_final_1 = input(f"Ingrese el marcador para la final 1 entre {partido_final_1.equipo1.nombre} vs {partido_final_1.equipo2.nombre} (separador por un -'): ")
    marcador_final_1_equipo1, marcador_final_1_equipo2 = map(int, marcador_final_1.split('-'))

    marcador_final_2 = input(f"Ingrese el marcador para la final 2 entre {partido_final_2.equipo1.nombre} vs {partido_final_2.equipo2.nombre} (separador por un -'): ")
    marcador_final_2_equipo1, marcador_final_2_equipo2 = map(int, marcador_final_2.split('-'))

    # Actualizar los puntos de los equipos según los marcadores de la final
    if marcador_final_1_equipo1 > marcador_final_1_equipo2:
        cuadrangular_1_top[0].puntos_cuadrangular_1 += 3
    elif marcador_final_1_equipo1 < marcador_final_1_equipo2:
        cuadrangular_1_top[1].puntos_cuadrangular_1 += 3
    else:
        cuadrangular_1_top[0].puntos_cuadrangular_1 += 1
        cuadrangular_1_top[1].puntos_cuadrangular_1 += 1

    if marcador_final_2_equipo1 > marcador_final_2_equipo2:
        cuadrangular_2_top[0].puntos_cuadrangular_2 += 3
    elif marcador_final_2_equipo1 < marcador_final_2_equipo2:
        cuadrangular_2_top[1].puntos_cuadrangular_2 += 3
    else:
        cuadrangular_2_top[0].puntos_cuadrangular_2 += 1
        cuadrangular_2_top[1].puntos_cuadrangular_2 += 1

    # Muestra la tabla de posiciones final por cuadrangular
    mostrar_tabla_posiciones_cuadrangular(cuadrangular_1)
    mostrar_tabla_posiciones_cuadrangular(cuadrangular_2)

    # Seleccionar los dos equipos con mayor cantidad de puntos de cada cuadrangular
    cuadrangular_1_top = sorted(cuadrangular_1, key=lambda x: x.puntos_cuadrangular_1, reverse=True)[:1]
    cuadrangular_2_top = sorted(cuadrangular_2, key=lambda x: x.puntos_cuadrangular_2, reverse=True)[:1]

    # Hacer un partido entre los dos equipos con mayor cantidad de puntos de cada cuadrangular
    partido_final = Partido(cuadrangular_1_top[0], cuadrangular_2_top[0])
    
    # Simular los partidos de la final
    marcador_final = input(f"Ingrese el marcador para la final entre {partido_final.equipo1.nombre} vs {partido_final.equipo2.nombre} (separador por un -''): ")
    marcador_final_equipo1, marcador_final_equipo2 = map(int, marcador_final.split('-'))

    # Actualizar los puntos de los equipos según los marcadores de la final
    if marcador_final_equipo1 > marcador_final_equipo2:
        cuadrangular_1_top[0].puntos_cuadrangular_1 += 3
    elif marcador_final_equipo1 < marcador_final_equipo2:
        cuadrangular_2_top[0].puntos_cuadrangular_1 += 3
    else:
        cuadrangular_1_top[0].puntos_cuadrangular_1 += 1
        cuadrangular_2_top[0].puntos_cuadrangular_1 += 1
    
    mostrar_tabla_posiciones(cuadrangular_1, cuadrangular_2)
    equipos_db.cerrar_conexion()    
    
if __name__ == "__main__":
    main()
