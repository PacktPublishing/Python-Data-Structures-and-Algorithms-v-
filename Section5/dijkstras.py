from Section2.stack import Stack
import sys


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

    def _min_distance(self, distance, fringe):
        # Initilaize minimum distance for next node
        min = sys.maxint

        # Search not nearest vertex not in the
        # shortest path tree
        for vertex in self._vertices:
            if distance[vertex][0] < min and vertex in fringe:
                min = distance[vertex][0]
                min_vertex = vertex

        return min_vertex

    def dijkstras(self, source, dest):

        # Initialize the distance of all nodes to infinity.
        distance = [(sys.maxint, -1)] * len(self._vertices)

        # The distance of source from source is 0.
        distance[source] = (0, 0)

        # Initially none of the nodes are visited.
        visited = [False] * len(self._vertices)

        # The fringe is only the source.
        fringe = [source]

        # While there are still entries in the fringe.
        while fringe:
            # Find the node with the minimum distance in the fringe as current vertex.
            current_vertex_key = self._min_distance(distance, fringe)

            # Remove the minimum distance node from fringe and mark it visited.
            fringe.remove(current_vertex_key)
            visited[current_vertex_key] = True
            current_vertex = self.get_vertex(current_vertex_key)

            # For all the neighbors of the current vertex, if the node is not visited already and is not in fringe, add it to the fringe.
            # Determine if the distance of the neighbour is already greater than it's existing distance +
            # the weight of the neighbour from teh current node. If so, change it.
            for neighbor in current_vertex.get_connections():
                neighbor_vertex = neighbor[0].get_key()
                neighbor_weight = neighbor[1]

                if neighbor_vertex not in fringe and not visited[neighbor_vertex]:
                    fringe.append(neighbor_vertex)

                if distance[neighbor_vertex][0] > distance[current_vertex_key][0] + neighbor_weight:
                    distance[neighbor_vertex] = (distance[current_vertex_key][0] + neighbor_weight, current_vertex_key)

        # Find the shortest path.
        s = Stack()
        x = dest
        while x != source:
            s.push(x)
            x = distance[x][1]
        s.push(x)

        shortest_path = []
        while not s.isEmpty():
            shortest_path.append(s.pop())

        return shortest_path, distance[dest][0]

if __name__ == "__main__":

    """
    graph = {
        "0" : [("1", 5), ("2", 3)],
        "1" : [("3", 3)],
        "2" : [("1", 1), ("3", 2), ("4", 6)],
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
    g.add_edge(2, 1, 1)
    g.add_edge(2, 3, 2)
    g.add_edge(2, 4, 6)
    g.add_edge(4, 3, 1)

    source = 0
    dest = 3
    (shortest_path, weight) = g.dijkstras(source, dest)

    print("Shortest distance between {} and {} in the graph follows this path: {} and has weight: {}"
        .format(source, dest, shortest_path, weight))
