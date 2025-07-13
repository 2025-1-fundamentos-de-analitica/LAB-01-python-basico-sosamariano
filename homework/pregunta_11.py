"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    archivo = "files/input/data.csv"
    suma_letras = {}

    with open(archivo, newline='', encoding='utf-8') as f:
        lector = csv.reader(f, delimiter='\t')
        for fila in lector:
            valor = int(fila[1])
            letras = fila[3].split(',')
            for letra in letras:
                suma_letras[letra] = suma_letras.get(letra, 0) + valor

    return dict(sorted(suma_letras.items()))
