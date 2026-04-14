from src.graph import build_conflict_graph

def greedy_coloring(graph):
    result = {}

    # Use a fixed order (sorted for consistency)
    nodes = sorted(graph.keys())

    for node in nodes:
        # Find colors used by neighbors
        used_colors = set()
        for neighbor in graph[node]:
            if neighbor in result:
                used_colors.add(result[neighbor])

        # Assign smallest available color
        color = 0
        while color in used_colors:
            color += 1

        result[node] = color

    return result


# Test
if __name__ == "__main__":
    enrollments = {
    "S1": ["C1", "C2"],
    "S2": ["C2", "C3"],
    "S3": ["C3", "C4"],
    "S4": ["C4", "C1"],
    "S5": ["C1", "C3"]
    }

    graph = build_conflict_graph(enrollments)
    result = greedy_coloring(graph)

    print("Greedy Coloring:")
    for course in result:
        print(course, ":", result[course])