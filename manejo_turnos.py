from constantes import *
from validacion_datos import *


def pedir_posicion(leyenda):
    ficha_elejida = input(leyenda)
    while not ingreso_valido(ficha_elejida):
        ficha_elejida = input(leyenda)
    return ficha_elejida


def jugada():
    """
    Pide las posiciones del tablero que se darán vuelta y si las fichas son
    distintas, devuelve un booleano que ayuda definir el cabio de turno.
    Autor: Galvan Nicolas
    """
    primera_ficha = pedir_posicion("1ra. Posicion: ")
    modificar_tablero(int(primera_ficha))
    segunda_ficha = pedir_posicion("2da. Posicion: ") 
    modificar_tablero(int(segunda_ficha))

    return (primera_ficha, segunda_ficha)

def modificar_tablero(ficha_elejida):
    """Da vuelta la ficha del tablero.
    Autor: Jaldin Omar
    """
    tablero[ficha_elejida + AJUSTE_DE_INDICE] = FICHAS[ficha_elejida + AJUSTE_DE_INDICE]
    imprimir_tablero()


def hay_que_cambiar_de_turno(primera_eleccion, segunda_eleccion):
    """
    Si las fichas correspondientes a las posiciones elegidas son distintas,
    se vuelven a dar vuelta. Oringina un booleano que ayuda definir el cabio
    de turno.
    Autor: Jaldin Omar
    """
    cambio_de_turno = False
    primera_ficha = int(primera_eleccion) + AJUSTE_DE_INDICE
    segunda_ficha = int(segunda_eleccion) + AJUSTE_DE_INDICE
    if tablero[primera_ficha] != tablero[segunda_ficha]:
        tablero[primera_ficha], tablero[segunda_ficha] = int(primera_eleccion), int(segunda_eleccion)
        cambio_de_turno = True
    
    return cambio_de_turno


def imprimir_tablero():
    """Imprime el tablero.
    Autor: Pascual Walter
    """

    imp_tablero = f"Fichas y Posiciones:"
    for columna in range(CANTIDAD_DE_COLUMNAS):
        imp_tablero += f"[{tablero[columna]}]".center(7)
    print(imp_tablero, "\n")
    for linea in range(CANTIDAD_DE_COLUMNAS, len(tablero), CANTIDAD_DE_COLUMNAS):
        imp_tablero = ""
        for columna in range(linea, linea + CANTIDAD_DE_COLUMNAS):
            imp_tablero += f"[{tablero[columna]}]".center(7)

        print(f"                    {imp_tablero}\n")
