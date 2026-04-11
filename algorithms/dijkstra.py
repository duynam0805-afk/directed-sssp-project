import heapq
import math

def dijkstra(n, adj, src):
    dist = [math.inf] * n
    dist[src] = 0

    pq = [(0, src)]

    heap_ops = 0
    relax = 0

    while pq:
        d, u = heapq.heappop(pq)
        heap_ops += 1

        if d != dist[u]:
            continue

        for v, w in adj[u]:
            nd = d + w

            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
                heap_ops += 1
                relax += 1

    return dist, relax, heap_ops