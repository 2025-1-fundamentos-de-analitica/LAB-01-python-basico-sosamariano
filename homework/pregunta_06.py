"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    archivo = "files/input/data.csv"
    valores = {}

    with open(archivo, newline='', encoding='utf-8') as f:
        lector = csv.reader(f, delimiter='\t')
        for fila in lector:
            columna_5 = fila[4].split(',')
            for par in columna_5:
                clave, valor = par.split(':')
                valor = int(valor)
                if clave not in valores:
                    valores[clave] = (valor, valor)
                else:
                    vmin, vmax = valores[clave]
                    valores[clave] = (min(vmin, valor), max(vmax, valor))

    resultado = [(clave, valores[clave][0], valores[clave][1]) for clave in sorted(valores)]
    return resultado
