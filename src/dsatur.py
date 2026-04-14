from src.graph import build_conflict_graph
def dsatur_coloring(graph):
    colors={}
    saturation={node: 0 for node in graph}
    degrees={node: len(graph[node]) for node in graph}
    while len(colors)<len(graph):
        #Selection of node with highest saturation
        uncolored=[node for node in graph if node not in colors]
        node=max(uncolored, key=lambda x: (saturation[x], degrees[x]))

        #Find used colors in neighbours
        used_color=set()
        for neighbour in graph[node]:
            if neighbour in colors:
                used_color.add(colors[neighbour])
        
        #Assigning smallest available color
        color=0
        while color in used_color:
            color+=1
        colors[node]=color
        #Update saturation of neighbours
        for neighbour in graph[node]:
            if neighbour not in colors:
                neighbour_colors=set(colors[n] for n in graph[neighbour] if n in colors)
                saturation[neighbour]=len(neighbour_colors)
    
    return colors

#Test
if __name__=="__main__":
    enrollments = {
    "S1": ["C1", "C2"],
    "S2": ["C2", "C3"],
    "S3": ["C3", "C4"],
    "S4": ["C4", "C1"],
    "S5": ["C1", "C3"]
    }
    graph=build_conflict_graph(enrollments)
    result=dsatur_coloring(graph)

    print("DSATUR Coloring:")
    for course in result:
        print(course, ":", result[course])
