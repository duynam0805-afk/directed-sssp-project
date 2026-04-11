import math

def bellman_ford(n, adj, src):
    dist = [math.inf] * n
    dist[src] = 0

    relax = 0
    iterations = 0

    for _ in range(n - 1):
        updated = False
        iterations += 1

        for u in range(n):
            if dist[u] == math.inf:
                continue

            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    relax += 1
                    updated = True

        if not updated:
            break

    return dist, relax, iterations