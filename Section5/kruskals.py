from Section5.union_find import UnionFind


class Vertex:
    """
    An example implementation of a Vertex or Node of a graph.
    """
    def __init__(self, key):
        """
        Creates a new Vertex.
        """
        self._neighbors = []
        self._key = key

    def add_neighbor(self, neighbor_vertex, weight):
        self._neighbors.append((neighbor_vertex, weight))

    def get_connections(self):
        return self._neighbors

    def get_key(self):
        return self._key

    def get_weight(self, to_vertex):
        for neighbor in self._neighbors:
            if to_vertex == neighbor[0].get_key():
                return neighbor[1]


class Graph:
    """
    An example implementation of Directed Graph ADT.
    """
    def __init__(self):
        """
        Creates a new, empty Graph.
        """
        self._vertices = {}

    def add_vertex(self, vertex):
        """
        Adds a new vertex into the graph.
        :param vertex: The Vertex to be added into the Graph.
        :return: None.
        """
        v = Vertex(vertex)
        self._vertices[vertex] = v

    def add_edge(self, from_vertex, to_vertex, weight):
        """
        Add a directed edge between two vertices
        :param from_vertex: Starting vertex of the edge
        :param to_vertex: Where the edge ends.
        :param weight: weight of the edge
        :return: None
        """
        if from_vertex not in self._vertices:
            self.add_vertex(from_vertex)

        if to_vertex not in self._vertices:
            self.add_vertex(to_vertex)

        self._vertices[from_vertex].add_neighbor(self._vertices[to_vertex], weight)

    def get_vertices(self):
        """
        Get all the vertices of the directed Graph.
        :return: List of vertices of the graph.
        """
        vertices = self._vertices.keys()
        vertices.sort()
        return vertices

    def get_edges(self):
        """
        Get all the edges of the directed graph.
        :return: List of edges of the graph.
        """
        edges = []
        for vertex in self._vertices:
            neighbors = self._vertices[vertex].get_connections()
            for neighbor in neighbors:
                edges.append((vertex, neighbor[0].get_key(), self._vertices[vertex].get_weight(neighbor[0].get_key())))

        return edges

    def get_vertex(self, vertex_key):
        for vertex in self._vertices:
            if vertex == vertex_key:
                return self._vertices[vertex]

        return None

    def kruskals(self):
        # Placeholder for the resulting minimum spanning tree
        result = []

        # Initialize the union-find data structure with an initial state
        # of all vertices being in distinct disjoint sets..
        no_of_vertices = len(self._vertices)
        uf = UnionFind(no_of_vertices)

        # Sort the edges in increasing order based on the weight.
        edges = sorted(self.get_edges(), key=lambda x: x[2])

        # Choose one edge at a time from the sorted list of edges.
        for edge in edges:
            vertex1 = edge[0]
            vertex2 = edge[1]

            # Check if the vertices of the edge are in same disjoint set.
            # If not, call an union, merge them to the same disjoint set.
            # Add the edge to result.
            if uf.find(vertex1) != uf.find(vertex2):
                uf.union(vertex1, vertex2)

                result.append(edge)

            # Optimize the algorithm by stopping when the number of edges
            # in result is n - 1.
            if len(result) == no_of_vertices - 1:
                break

        # Return the resulting minimum spanning tree.
        return result

if __name__ == "__main__":

    """
    # Graph constructed as a directed graph removing redundant edges
    graph = {
        "0" : [("1", 1), ("2", 2), ("3", 3)],
        "1" : [("2", 1)],
        "2" : [],
        "3" : [("2", 6)]
    }
    """

    g = Graph()

    for v in range(4):
        g.add_vertex(v)

    g.add_edge(0, 1, 1)
    g.add_edge(0, 2, 2)
    g.add_edge(0, 3, 3)
    g.add_edge(1, 2, 1)
    g.add_edge(3, 2, 6)

    m_spanning_tree_edges = g.kruskals()

    print("The edges in the minimum spanning tree are: {}"
        .format(m_spanning_tree_edges))
