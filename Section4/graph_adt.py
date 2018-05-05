class Vertex:
    """
    An example implementation of a Vertex or Node of a graph.
    """
    def __init__(self, key):
        """
        Creates a new Vertex.
        :param key: Vertex Identifier
        """
        pass

class Graph:
    """
    An example implementation of Directed Graph ADT.
    """
    def __init__(self):
        """
        Creates a new, empty Graph.
        """
        pass

    def add_vertex(self, vertex):
        """
        Adds a new vertex into the graph.
        :param vertex: The Vertex to be added into the Graph.
        :return: None.
        """
        pass

    def add_edge(self, from_vertex, to_vertex, weight):
        """
        Add a directed edge between two vertices
        :param from_vertex: Starting vertex of the edge
        :param to_vertex: Where the edge ends.
        :param weight: weight of the edge
        :return: None
        """
        pass

    def get_vertices(self):
        """
        Get all the vertices of the directed Graph.
        :return: List of vertices of the graph.
        """
        pass

    def get_edges(self):
        """
        Get all the edges of the directed graph.
        :return: List of edges of the graph.
        """
        pass


if __name__ == "__main__":

    """
    graph = {
        "0" : [("1", 5), ("2", 3)],
        "1" : [("3", 3)],
        "2" : [("1", 2), ("3", 5), ("4", 6)],
        "3" : [],
        "4" : ["3", 1]
    }
    """

    g = Graph()

    for v in range(5):
        g.add_vertex(v)

    g.add_edge(0, 1, 5)
    g.add_edge(0, 2, 3)
    g.add_edge(1, 3, 3)
    g.add_edge(2, 1, 2)
    g.add_edge(2, 3, 5)
    g.add_edge(2, 4, 6)
    g.add_edge(4, 3, 1)

    print(g.get_vertices())
    print(g.get_edges())
