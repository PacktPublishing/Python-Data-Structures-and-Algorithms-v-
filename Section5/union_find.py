class UnionFind:
    def __init__(self, n):
        self._n = n
        self._parent = [i for i in range(n)]
        self._rank = [0 for _ in range(n)]

    # Returns representative of the set with element x
    def find(self, x):

        # if x is not the parent of itelf
        if(x != self._parent[x]):
            # We recursively find the parent of x.
            # And at each step back we optmize the data structure to hold
            # each node along the path under the representative.
            self._parent[x] = self.find(self._parent[x])

        return self._parent[x]

    def union(self, x, y):
        # Find the root of x and y
        (x_root, y_root) = (self.find(x), self.find(y))

        # If the are part of same set, they are already connected.
        if x_root == y_root:
            return

        # Move the node with lesser rank under the node with higher rank.
        if self._rank[x_root] < self._rank[y_root]:
            self._parent[x_root] = y_root
        elif self._rank[y_root] < self._rank[x_root]:
            self._parent[y_root] = x_root
        else:
            # If the rank is same, pick one representative and increment its rank.
            self._parent[y_root] = x_root
            self._rank[x_root] += 1

    def __str__(self):
        return str(self._parent)

if __name__ == "__main__":
    uf = UnionFind(4)
    print("Initial state: {}".format(uf))

    uf.union(0, 3)
    print("State after union(0,3): {}".format(uf))

    uf.union(1, 2)
    print("State after union(1,2): {}".format(uf))

    uf.union(3, 2)
    print("State after union(3, 2): {}".format(uf))

    print("The representative of set having node 2 is: {}".format(uf.find(2)))

    print("State after find(2): {}".format(uf))


