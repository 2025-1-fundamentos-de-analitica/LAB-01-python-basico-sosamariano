"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    archivo = "files/input/data.csv"
    suma_columna = 0
    
    with open(archivo, newline='', encoding='utf-8') as f:
        lector = csv.reader(f, delimiter='\t')
        for fila in lector:
            suma_columna += int(fila[1])
    
    return suma_columna
