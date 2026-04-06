import time

from utils.graph_generator import generate_graph
from algorithms.dijkstra import dijkstra
from algorithms.bellman_ford import bellman_ford
from algorithms.frontier import frontier_sssp


def run_single_experiment(n, m):
    graph = generate_graph(n, m)
    source = 0

    print(f"\nGraph: n={n}, m={m}")
    print("-" * 50)

    start = time.time()
    _, d_relax, d_heap = dijkstra(graph, source)
    d_time = time.time() - start

    start = time.time()
    _, bf_relax, bf_iter = bellman_ford(graph, source)
    bf_time = time.time() - start

    start = time.time()
    _, f_relax, f_rounds = frontier_sssp(graph, source)
    f_time = time.time() - start

    print("Dijkstra:")
    print(f"  Relaxations: {d_relax}")
    print(f"  Heap operations: {d_heap}")
    print(f"  Time: {d_time:.4f}s")

    print("\nBellman-Ford:")
    print(f"  Relaxations: {bf_relax}")
    print(f"  Iterations: {bf_iter}")
    print(f"  Time: {bf_time:.4f}s")

    print("\nFrontier-based SSSP:")
    print(f"  Relaxations: {f_relax}")
    print(f"  Rounds: {f_rounds}")
    print(f"  Time: {f_time:.4f}s")


def main():
    run_single_experiment(400, 2000)

    for n in [200, 500, 1000]:
        m = n * 5
        run_single_experiment(n, m)


if __name__ == "__main__":
    main()