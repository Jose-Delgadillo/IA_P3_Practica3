"""
Simulador gráfico de Dijkstra (mínimo)
Usando solo la biblioteca estándar de Python

Este código presenta un pequeño grafo fijo con 6 nodos y sus conexiones.
Se muestra una interfaz con botones para ejecutar el algoritmo de Dijkstra paso a paso.

Muestra un pequeño grafo con 6 nodos (A a F) y pesos.

Usa colores:
Amarillo para el nodo actual.
Verde claro para los nodos ya visitados.

Al presionar "Paso", ejecuta una iteración del algoritmo de Dijkstra.
Al presionar "Reiniciar", empieza desde cero.
"""

import tkinter as tk
from tkinter import messagebox

# --- Datos del grafo ---
# Formato: nodo : [(vecino, peso)]
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('C', 6), ('D', 1)],
    'C': [('A', 5), ('B', 6), ('D', 3), ('E', 8)],
    'D': [('B', 1), ('C', 3), ('E', 4), ('F', 2)],
    'E': [('C', 8), ('D', 4), ('F', 1)],
    'F': [('D', 2), ('E', 1)],
}

positions = {
    'A': (50, 100),
    'B': (150, 50),
    'C': (150, 150),
    'D': (250, 100),
    'E': (350, 150),
    'F': (350, 50)
}

# --- Dijkstra paso a paso ---
class DijkstraSimulator:
    def __init__(self, canvas):
        self.canvas = canvas
        self.reset()

    def reset(self):
        self.dist = {node: float('inf') for node in graph}
        self.prev = {node: None for node in graph}
        self.visited = set()
        self.queue = list(graph.keys())
        self.current = 'A'
        self.dist[self.current] = 0
        self.draw_graph()

    def step(self):
        if not self.queue:
            messagebox.showinfo("Finalizado", "Todos los nodos han sido visitados.")
            return

        # Escoger el nodo no visitado con menor distancia
        self.current = min((n for n in self.queue if n not in self.visited), key=lambda x: self.dist[x], default=None)
        if self.current is None:
            messagebox.showinfo("Finalizado", "No hay más nodos alcanzables.")
            return

        self.visited.add(self.current)

        for neighbor, weight in graph[self.current]:
            if neighbor in self.visited:
                continue
            new_dist = self.dist[self.current] + weight
            if new_dist < self.dist[neighbor]:
                self.dist[neighbor] = new_dist
                self.prev[neighbor] = self.current

        self.draw_graph()

    def draw_graph(self):
        self.canvas.delete("all")

        # Dibujar aristas
        for node in graph:
            x1, y1 = positions[node]
            for neighbor, weight in graph[node]:
                x2, y2 = positions[neighbor]
                self.canvas.create_line(x1, y1, x2, y2, fill="gray", width=2)
                mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                self.canvas.create_text(mx, my, text=str(weight), fill="black", font=("Arial", 8))

        # Dibujar nodos
        for node in graph:
            x, y = positions[node]
            color = "white"
            if node in self.visited:
                color = "lightgreen"
            elif node == self.current:
                color = "yellow"
            self.canvas.create_oval(x-20, y-20, x+20, y+20, fill=color, outline="black", width=2)
            self.canvas.create_text(x, y, text=node + f"\n{self.dist[node] if self.dist[node] < float('inf') else '∞'}", font=("Arial", 10))

# --- Interfaz ---
def main():
    root = tk.Tk()
    root.title("Simulador de Dijkstra (Gráfico sin librerías externas)")

    canvas = tk.Canvas(root, width=420, height=220, bg="white")
    canvas.pack(padx=10, pady=10)

    sim = DijkstraSimulator(canvas)

    button_frame = tk.Frame(root)
    button_frame.pack()

    tk.Button(button_frame, text="Paso", command=sim.step).pack(side="left", padx=5)
    tk.Button(button_frame, text="Reiniciar", command=sim.reset).pack(side="left", padx=5)
    tk.Button(button_frame, text="Salir", command=root.destroy).pack(side="left", padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()
