from src.graph import build_conflict_graph

def is_safe(node, graph, color, assignment):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def backtracking_coloring(graph, nodes, assignment, max_colors):
    if len(assignment) == len(nodes):
        return True

    node = nodes[len(assignment)]

    for color in range(max_colors):
        if is_safe(node, graph, color, assignment):
            assignment[node] = color

            if backtracking_coloring(graph, nodes, assignment, max_colors):
                return True

            del assignment[node]

    return False


def solve_graph_coloring(graph):
    nodes = list(graph.keys())

    for max_colors in range(1, len(nodes) + 1):
        assignment = {}
        if backtracking_coloring(graph, nodes, assignment, max_colors):
            return assignment

    return None


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
    result = solve_graph_coloring(graph)

    print("Optimal Coloring:")
    for course in result:
        print(course, ":", result[course])