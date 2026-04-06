import heapq

def dijkstra(graph, source):
    dist = {v: float('inf') for v in graph}
    dist[source] = 0

    heap = [(0, source)]

    relaxations = 0
    heap_ops = 0

    while heap:
        d, u = heapq.heappop(heap)
        heap_ops += 1

        if d > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                relaxations += 1
                heapq.heappush(heap, (dist[v], v))
                heap_ops += 1

    return dist, relaxations, heap_ops