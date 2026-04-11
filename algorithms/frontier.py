import math

def frontier_sssp(n, adj, src):
    dist = [math.inf] * n
    dist[src] = 0

    frontier = [src]

    relax = 0
    rounds = 0

    while frontier:
        next_frontier = []
        rounds += 1

        for u in frontier:
            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    relax += 1
                    next_frontier.append(v)

        frontier = next_frontier

    return dist, relax, rounds