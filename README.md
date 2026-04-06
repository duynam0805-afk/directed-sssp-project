```markdown
# Directed SSSP Beyond Dijkstra’s Sorting Barrier

## Authors
- Trương Mậu Anh - 23001498
- Bùi Phương Nam - 23001538

## Description
This project studies the Single-Source Shortest Path (SSSP) problem on directed graphs.

We implement and compare:
- Dijkstra's Algorithm (baseline)
- Bellman-Ford Algorithm
- Frontier-based SSSP (prototype inspired by recent research)

## Features
- Generate random directed graphs
- Measure:
  - Relaxations
  - Heap operations
  - Iterations / Rounds
- Compare algorithm performance

## Project Structure
directed-sssp-project/
│
├── run_experiment.py
├── algorithms/
│ ├── dijkstra.py
│ ├── bellman_ford.py
│ └── frontier.py
│
└── utils/
    └── graph_generator.py


## Requirements
```bash
pip install -r requirements.txt

##Run
python run_experiment.py

##Example Output
Graph: n=400, m=2000

Dijkstra:
  Relaxations: 2315
  Heap ops:    3180

Bellman-Ford:
  Relaxations: 15200
  Iterations:  399

Frontier Prototype:
  Relaxations: 2480
  Rounds:      17

#Notes
- Dijkstra uses a priority queue (heap) → sorting overhead
- Bellman-Ford performs many relaxations
- Frontier-based method:
Does NOT use priority queue
Uses rounds instead of exact ordering
Demonstrates idea of removing sorting barrier

##Future Work
- Add visualization (matplotlib)
- Implement Dial’s Algorithm (integer weights)
- Parallel shortest path algorithms

##Reference
Ran Duan et al. (2025)
Breaking the Sorting Barrier for Directed Single-Source Shortest Paths