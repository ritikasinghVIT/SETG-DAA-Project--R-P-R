import time
from src.graph import build_conflict_graph
from src.greedy import greedy_coloring
from src.backtracking import solve_graph_coloring
from src.dsatur import dsatur_coloring

def take_input():
    n = int(input("Enter number of students: "))
    enrollments = {}

    for i in range(n):
        student = f"S{i+1}"
        courses = input(f"Enter courses for {student} (space-separated): ").split()
        enrollments[student] = courses

    return enrollments


def run_comparison(enrollments):
    graph = build_conflict_graph(enrollments)

    results = {}

    # Greedy
    start = time.time()
    greedy_result = greedy_coloring(graph)
    end = time.time()
    results["Greedy"] = {
        "slots": max(greedy_result.values()) + 1,
        "time": round(end - start, 6)
    }

    # Backtracking
    start = time.time()
    backtracking_result = solve_graph_coloring(graph)
    end = time.time()
    results["Backtracking"] = {
        "slots": max(backtracking_result.values()) + 1,
        "time": end - start
    }

    # DSATUR
    start = time.time()
    dsatur_result = dsatur_coloring(graph)
    end = time.time()
    results["DSATUR"] = {
        "slots": max(dsatur_result.values()) + 1,
        "time": end - start
    }

    return results


# Test dataset
if __name__ == "__main__":
    enrollments = take_input()

    results = run_comparison(enrollments)

    print("Algorithm Comparison:")
    for algo in results:
        print(algo, "-> Slots:", results[algo]["slots"], ", Time:", results[algo]["time"])
    
    graph = build_conflict_graph(enrollments)

    print("Graph:")
    for k, v in graph.items():
        print(k, "->", v)