from benchmark import benchmark

def main():
    sizes = [200, 400, 800, 1200]

    all_results = {}

    for n in sizes:
        m = n * 5
        print(f"\nRunning n={n}, m={m}")
        res = benchmark(n, m, runs=5)
        all_results[n] = res

        print(res)

    return all_results


if __name__ == "__main__":
    main()