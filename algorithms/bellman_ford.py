def bellman_ford(graph, source):
    dist = {v: float('inf') for v in graph}
    dist[source] = 0

    relaxations = 0
    iterations = 0

    n = len(graph)

    for _ in range(n - 1):
        updated = False
        iterations += 1

        for u in graph:
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    relaxations += 1
                    updated = True

        if not updated:
            break

    return dist, relaxations, iterations