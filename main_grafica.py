import random
from grafica_inicio import interfaz_grafica_inicio

def main_grafica():
    """Función principal para la ejecución de la interfaz grafica
    Autor: Galvan Nicolas
    """
    lista_participantes = []
    lista_participantes = interfaz_grafica_inicio(lista_participantes)
    if lista_participantes == []:
        lista_participantes = ["Participante_1","Participante_2","Participante_3"]
    print("------------------------------------------------------------------------")
    print("PARTICIPANTES")
    print (lista_participantes)
    print("------------------------------------------------------------------------")
    random.shuffle(lista_participantes)
    return lista_participantes