"""
Simulador del Algoritmo de Dijkstra
Versión básica en consola (paso a paso)

Este código implementa el algoritmo de Dijkstra para encontrar el camino más corto
desde un nodo origen a todos los demás en un grafo con pesos no negativos.

Se muestran los pasos del algoritmo, incluyendo:
- El nodo actualmente procesado.
- Las distancias actualizadas a los nodos vecinos.
- El estado final con las distancias mínimas.

Observaciones:
- No se usa ninguna librería externa, solo estructuras básicas de Python.
- El grafo se representa como un diccionario de adyacencias con pesos.
"""

import heapq

def dijkstra(grafo, inicio):
    # Inicialización
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    visitados = set()
    cola = [(0, inicio)]

    print(f"Inicio en nodo '{inicio}'\n")

    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)

        if nodo_actual in visitados:
            continue

        print(f"Procesando nodo: {nodo_actual} (distancia acumulada: {distancia_actual})")
        visitados.add(nodo_actual)

        for vecino, peso in grafo[nodo_actual].items():
            if vecino in visitados:
                continue
            nueva_distancia = distancia_actual + peso
            if nueva_distancia < distancias[vecino]:
                print(f"  Actualizando distancia de {vecino}: {distancias[vecino]} → {nueva_distancia}")
                distancias[vecino] = nueva_distancia
                heapq.heappush(cola, (nueva_distancia, vecino))
            else:
                print(f"  No se actualiza {vecino}, distancia actual: {distancias[vecino]}")

        print()

    print("Distancias finales desde el nodo origen:")
    for nodo, distancia in distancias.items():
        print(f"  {nodo}: {distancia}")


# Ejemplo de uso
grafo = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
}

dijkstra(grafo, 'A')
