"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    
    archivo = "files/input/data.csv"
    conteo_letras = {}
    
    with open(archivo, newline='', encoding='utf-8') as f:
        lector = csv.reader(f, delimiter='\t')
        for fila in lector:
            letra = fila[0]
            if letra not in conteo_letras:
                conteo_letras[letra] = 0
            conteo_letras[letra] += int(fila[1])
    
    return sorted(conteo_letras.items(), key= lambda letra: letra[0])
