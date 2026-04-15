import matplotlib.pyplot as plt
from benchmark import benchmark


def plot():
    sizes = [1000, 5000, 10000, 20000, 30000, 50000]

    d_times, bf_times, f_times = [], [], []

    for n in sizes:
        m = n * 5
        res = benchmark(n, m, runs=5)

        d_times.append(res["dijkstra"]["time"])
        bf_times.append(res["bellman"]["time"])
        f_times.append(res["frontier"]["time"])

    plt.figure()

    plt.plot(sizes, d_times, marker='o', label="Dijkstra")
    plt.plot(sizes, bf_times, marker='o', label="Bellman-Ford")
    plt.plot(sizes, f_times, marker='o', label="Frontier")

    plt.xlabel("Number of nodes (n)")
    plt.ylabel("Time (seconds)")
    plt.title("SSSP Algorithm Comparison")
    plt.legend()

    plt.grid()
    plt.savefig("comparison.png")
    plt.show()


if __name__ == "__main__":
    plot()