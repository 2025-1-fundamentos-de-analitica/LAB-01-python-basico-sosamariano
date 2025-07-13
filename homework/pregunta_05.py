"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    
    archivo = "files/input/data.csv"
    registros = {}
    
    with open(archivo, newline='', encoding='utf-8') as f:
        lector = csv.reader(f, delimiter='\t')
        for fila in lector:
            letra = fila[0]
            valor = int(fila[1])

            if letra not in registros:
                registros[letra] = (valor, valor)
            else:
                max_actual, min_actual = registros[letra]
                registros[letra] = (max(max_actual, valor), min(min_actual, valor))
    
    resultado = [(clave, valor[0], valor[1]) for clave, valor in registros.items()]
    return sorted(resultado, key=lambda x: x[0])
