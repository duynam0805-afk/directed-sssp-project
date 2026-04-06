def frontier_sssp(graph, source):
    dist = {v: float('inf') for v in graph}
    dist[source] = 0

    frontier = [source]

    relaxations = 0
    rounds = 0

    while frontier:
        next_frontier = []
        rounds += 1

        for u in frontier:
            for v, w in graph[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    relaxations += 1
                    next_frontier.append(v)

        frontier = next_frontier

    return dist, relaxations, rounds