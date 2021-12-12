from constantes import *


def ingreso_valido(entrada_usuario):
    """Verifica que el valor ingresado cumpla con los requisitos.
    Autor: Pibernus Tomas
    """
    validez = True
    if not (es_numero(entrada_usuario)):
        print(f"El valor ingresado no es un número, ingrese un valor válido.")
        validez = False

    elif not rango_valido(int(entrada_usuario)):
        print(f"El valor ingresado no corresponde a una posición del tablero, ingrese un valor válido.")
        validez = False
    elif not esta_disponible(entrada_usuario):
        print(f"El valor ingresado no está disponible.")
        validez = False

    return validez


def es_numero(valor_elegido):
    """Verifica que el valor ingresado sea un número.
    Autor: Tineo Javier
    """

    return valor_elegido.isnumeric()


def rango_valido(valor_elegido):
    """Verifica que el valor ingresado corresponda a una posición del tablero.
    Autor: Pibernus Tomas
    """
    longitud_tablero = len(tablero)

    return not (valor_elegido > longitud_tablero or valor_elegido < MINIMO_VALOR_FICHA)


def esta_disponible(valor):
    """Verifica que el valor ingresado se encuentre disponible.
    Autor: Tineo Javier
    """

    return tablero[int(valor) + AJUSTE_DE_INDICE] != FICHAS[int(valor) + AJUSTE_DE_INDICE]
