from graph import build_conflict_graph
def greedy_coloring(graph):
    result={}
    for node in graph:
        #Colors used by neighbours
        used_colors=set()
        for neighbour in graph[node]:
            if neighbour in result:
                used_colors.add(result[neighbour])
        #Assigning smallest available color
        color=0
        while color in used_colors:
            color+=1
        result[node]=color
    return result

#Test
if __name__=="__main__":
    enrollments={
        "S1": ["C1", "C2"],
        "S2": ["C1", "C3"],
        "S3": ["C2", "C3"],
        "S4": ["C2", "C4"]
    }
    graph=build_conflict_graph(enrollments)
    coloring=greedy_coloring(graph)
    print("Course->Slot Assignment:")
    for course in coloring:
        print(course, ":", coloring[course])
