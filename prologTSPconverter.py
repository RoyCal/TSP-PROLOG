# Esse código irá converter uma lista de arestas no formato Prolog para uma matriz de adjacência 
# que poderá ser usada no código TSP.py

import math
import re

def edges_to_matrix(edge_lines):
    # Expressão regular para capturar edge(u, v, w).
    pattern = re.compile(r"edge\((\w+),\s*(\w+),\s*(\d+)\)\.")
    edges = []
    nodes = set()

    # Lê cada linha e extrai os dados
    for line in edge_lines:
        match = pattern.match(line.strip())
        if match:
            u, v, w = match.groups()
            w = int(w)
            edges.append((u, v, w))
            nodes.add(u)
            nodes.add(v)

    # Ordena os nós para ter índices consistentes
    nodes = sorted(nodes)
    index = {node: i for i, node in enumerate(nodes)}

    n = len(nodes)
    # Inicializa matriz com infinito
    mat = [[math.inf]*n for _ in range(n)]

    # Distância de um nó para si mesmo = 0
    for i in range(n):
        mat[i][i] = 0

    # Preenche as distâncias das arestas
    for u, v, w in edges:
        i, j = index[u], index[v]
        mat[i][j] = w

    return mat, nodes

# ---------------- LISTA DE ARESTAS PROLOG ----------------
edge_lines = [
    "edge(a, b, 5900).",
    "edge(a, c, 6200).",
    "edge(a, d, 7900).",
    "edge(a, e, 5200).",
    "edge(a, f, 4900).",
    "edge(a, g, 6300).",
    "edge(a, h, 8000).",
    "edge(b, a, 6700).",
    "edge(b, c, 6200).",
    "edge(b, d, 4200).",
    "edge(b, e, 4500).",
    "edge(b, f, 7000).",
    "edge(b, g, 5300).",
    "edge(b, h, 5900).",
    "edge(c, a, 7500).",
    "edge(c, b, 5700).",
    "edge(c, d, 9400).",
    "edge(c, e, 4000).",
    "edge(c, f, 4100).",
    "edge(c, g, 10500).",
    "edge(c, h, 650).",
    "edge(d, a, 7500).",
    "edge(d, b, 4300).",
    "edge(d, c, 10200).",
    "edge(d, e, 8500).",
    "edge(d, f, 11600).",
    "edge(d, g, 1900).",
    "edge(d, h, 9800).",
    "edge(e, a, 5200).",
    "edge(e, b, 4700).",
    "edge(e, c, 2200).",
    "edge(e, d, 8400).",
    "edge(e, f, 4000).",
    "edge(e, g, 9500).",
    "edge(e, h, 4100).",
    "edge(f, a, 6700).",
    "edge(f, b, 6500).",
    "edge(f, c, 3600).",
    "edge(f, d, 10200).",
    "edge(f, e, 4000).",
    "edge(f, g, 11200).",
    "edge(f, h, 4400).",
    "edge(g, a, 4900).",
    "edge(g, b, 5600).",
    "edge(g, c, 10100).",
    "edge(g, d, 1900).",
    "edge(g, e, 11800).",
    "edge(g, f, 8900).",
    "edge(g, h, 11100).",
    "edge(h, a, 7900).",
    "edge(h, b, 6100).",
    "edge(h, c, 250).",
    "edge(h, d, 9800).",
    "edge(h, e, 4500).",
    "edge(h, f, 3800).",
    "edge(h, g, 10900)."
]

mat, nodes = edges_to_matrix(edge_lines)

print("Ordem dos nós:", nodes)
for row in mat:
    print(row)
