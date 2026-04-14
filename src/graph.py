def build_conflict_graph(enrollments):
    graph={}

    #Initialize Graph
    for courses in enrollments.values():
        for course in courses:
            if course not in graph:
                graph[course]=set()
    
    #Add edges
    for courses in enrollments.values():
        for i in range(len(courses)):
            for j in range(i+1, len(courses)):
                c1, c2 = courses[i], courses[j]
                graph[c1].add(c2)
                graph[c2].add(c1)
    
    return graph

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
    for course in graph:
        print(Course, ":", list(graph[course]))