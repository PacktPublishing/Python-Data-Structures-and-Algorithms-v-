
# Undirected Graph from demo represented as Adjacency List
graph = {
    "a": [("b", 7), ("c", 9), ("f", 14)],
    "b": [("a", 7), ("c", 10), ("d", 15)],
    "c": [("a", 9), ("b", 10), ("d", 11), ("f", 2)],
    "d": [("b", 15), ("c", 11), ("e", 6)],
    "e": [("d", 6), ("f", 9)],
    "f": [("a", 14), ("c", 2), ("e", 9)],
}

def find_vertices():
    return graph.keys()

def find_edges():
    edges = []
    for v in graph:
        for e in graph[v]:
            edges.append((v, e[0], e[1]))

    return edges

print("Vertices: {}".format(find_vertices()))
print("Edges: {}".format(find_edges()))