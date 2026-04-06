import random

def generate_graph(n, m, weight_range=(1, 10)):
    graph = {i: [] for i in range(n)}

    edges = set()
    while len(edges) < m:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v:
            edges.add((u, v))

    for (u, v) in edges:
        w = random.randint(*weight_range)
        graph[u].append((v, w))

    return graph