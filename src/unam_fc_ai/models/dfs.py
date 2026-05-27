"""
=============================================================================
UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO (UNAM)
Facultad de Ciencias
Materia: Inteligencia Artificial
Docente: Dra. Jessica Sarahi Méndez Rincón
Ayudante de Laboratorio: Diego Eduardo Peña Villegas
Alumno: Diego Hazael Vega Alonso
Año escolar: 2026-2
Copyright: (c) 2025 UNAM - MIT License
Version: 1.0
This software is for educational purposes. 
The accuracy of the models depends strictly on the quality 
and preprocessing of the input data.
-----------------------------------------------------------------------------
UNAM IA Library: A professional toolkit for AI developed at UNAM.
=============================================================================
"""
import time


def dfs(grafo, nodo, visitados=None):
    """
    Algoritmo Depth-First Search (DFS).
    Parámetros:
    grafo: diccionario que representa el grafo (lista de adyacencia)
    nodo: nodo inicial desde donde comienza la búsqueda
    visitados: conjunto de nodos ya visitados
    Retorna:
    conjunto de nodos visitados
    """
    if visitados is None:
        visitados = set()
    # Marcar nodo en el que estamos como visitado y lo procesamos (en este caso, imprimimos su valor)
    visitados.add(nodo)
    print(nodo, end=" ")
    # Exploraramos los vecinos del nodo actual
    for vecino in grafo.get(nodo, []):
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)
    return visitados


def ejecutar_dfs(grafo, inicio):
    """
    Ejecuta el agoritmo DFS y mide el tiempo de ejecución.
    """
    inicio_tiempo = time.time()
    visitados = dfs(grafo, inicio)
    fin_tiempo = time.time()
    print("\n")
    print("Nodos visitados:", visitados)
    print("Tiempo de ejecución:", fin_tiempo - inicio_tiempo, "segundos")


# Ejemplo de grafo
grafo = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}


ejecutar_dfs(grafo, 2)