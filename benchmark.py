import time
from utils.graph_generator import generate_graph
from algorithms.dijkstra import dijkstra
from algorithms.bellman_ford import bellman_ford
from algorithms.frontier import frontier_sssp


def benchmark(n, m, runs=5):
    results = {
        "dijkstra": {"time": 0, "relax": 0, "heap": 0},
        "bellman": {"time": 0, "relax": 0, "iter": 0},
        "frontier": {"time": 0, "relax": 0, "rounds": 0},
    }

    for _ in range(runs):
        graph = generate_graph(n, m)
        src = 0

        # Dijkstra
        start = time.time()
        _, r, h = dijkstra(n, graph, src)
        results["dijkstra"]["time"] += time.time() - start
        results["dijkstra"]["relax"] += r
        results["dijkstra"]["heap"] += h

        # Bellman-Ford
        start = time.time()
        _, r, it = bellman_ford(n, graph, src)
        results["bellman"]["time"] += time.time() - start
        results["bellman"]["relax"] += r
        results["bellman"]["iter"] += it

        # Frontier
        start = time.time()
        _, r, rd = frontier_sssp(n, graph, src)
        results["frontier"]["time"] += time.time() - start
        results["frontier"]["relax"] += r
        results["frontier"]["rounds"] += rd

    # average
    for algo in results:
        for key in results[algo]:
            results[algo][key] /= runs

    return results