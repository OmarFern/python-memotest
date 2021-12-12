import random
import time
from constantes import *
from main_grafica import *
from validacion_datos import *
from resultado_partida import *

def dicc_participantes(lista_participantes):
    """arma un diccionario con el turno como clave y nombre del jugador, puntos, jugadas
    como valores"""
    participantes = {}
    pos = 1
    for i in lista_participantes:
        participantes[pos] = [i,0,0]
        pos += 1
    return participantes



def empezar_juego():
    """Ejecuta el juego, crea un diccionario que lleva la cuena de los puntos,
    jugadas y turno.
    Autor: Varios -> Jaldin Omar
    """
    lista_participantes = main_grafica()
    participantes = dicc_participantes(lista_participantes)
    #random.shuffle(FICHAS)41
    inicio = time.time()
    turno = 1
    while FICHAS != tablero:
        jugador_actual = participantes[turno][JUGADOR]
        print(f"Turno de: {jugador_actual}!\n")
        participantes, turno = procesar_jugada(participantes, turno)

    final = time.time()
    tiempo_de_juego(inicio, final)
    intentos_realizados(datos)
    declarar_ganador(datos)


empezar_juego()
