from constantes import *


def mostrar_tiempo_de_juego(inicio, final):
    """Recibe el tiempo de inicio y final del juego. Imprime la duración del
    juego en horas, minutos y segundos segun corresponda.
    Autor: Lima Karen
    """

    tiempo = (final - inicio)
    if tiempo >= HORA_EN_SEGUNDOS:
        hora = tiempo // HORA_EN_SEGUNDOS
        minutos = int((tiempo - (hora * HORA_EN_SEGUNDOS)) // MINUTO_EN_SEGUNDOS)
        segundos = int(tiempo - (minutos * MINUTO_EN_SEGUNDOS))
        print(f"El juego duró {hora} horas, {minutos} minutos y {segundos} segundos.")

    elif tiempo >= MINUTO_EN_SEGUNDOS:
        minutos = int(tiempo // MINUTO_EN_SEGUNDOS)
        segundos = int(tiempo - (minutos * MINUTO_EN_SEGUNDOS))
        print(f"El juego duró {minutos} minutos y {segundos} segundos.")
    else:
        print(f"El juego duró {int(tiempo)} segundos.")
