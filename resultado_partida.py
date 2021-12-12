from constantes import *
from manejo_turnos import *


def desempate(datos):
    """Determina e imprime si hay un ganador en caso de igual cantidad de
    puntos.
    Autor: Tineo Javier
    """
    if datos[jugador_2][JUGADAS] < datos[jugador_1][JUGADAS]:
        print(f"El ganador es {jugador_2}, porque realizó menos intentos. Ambos jugadores obruvieron"
              f" {datos[jugador_2][PUNTOS]} puntos.")
    else:
        print(f"Hubo un empate, ambos jugadores obruvieron {datos[jugador_2][PUNTOS]} puntos.")


def declarar_ganador(datos):
    """Determina e imprime el ganador del juego en base a sus puntos y en caso
    de que sean iguales llama a "desempate".
    Autor: Lima Karen
    """

    if datos[jugador_1][PUNTOS] > datos[jugador_2][PUNTOS]:
        print(f"El ganador es {jugador_1} con {datos[jugador_1][PUNTOS]} puntos.")
    elif datos[jugador_2][PUNTOS] > datos[jugador_1][PUNTOS]:
        print(f"El ganador es {jugador_2} con {datos[jugador_2][PUNTOS]} puntos.")
    else:
        desempate(datos)


def procesar_jugada(participantes, turno):
    """Suma 1 al contador de jugadas del jugador actual y 1 al contador de
    puntos si las fichas son iguales. Define el cambio de turno.
    Autor: Pibernus Tomas
    """
    participantes[turno][JUGADAS] += 1
    imprimir_tablero()
    a,b = jugada()
    if hay_que_cambiar_de_turno(a,b):
        if turno < len(participantes):
            turno += 1
        else:
            turno = 1
    else:
        participantes[turno][PUNTOS] += 1

    return participantes, turno


def intentos_realizados(datos):
    """Imprime los intentos totales realizados.
    Autor: Lima Karen
    """
    jugadas = datos[jugador_1][JUGADAS] + datos[jugador_2][JUGADAS]
    print(f"Se realizaron un total de {jugadas} intentos.")
