"""
Basic implementation of the Graph structure. The implementation approach is based on 2D
list, which is fine for small graphs, where the size is known from advance. For large
graphs is better to use the nodes dictionary.
"""


from copy import deepcopy


class MatrixGraph:
    """This class provides a 2D array, which represents the example of a graph structure.
    We claim that indices (x, y) E (0, 1, 2, 3, 4, ..., size - 1) denote the graph nodes,
    respectively A, B, C, D, E, ... ?. Therefore G[x][y] = 1 means that there is an edge
    between two nodes x and y. On the other hand, G[x][y] = 0 means that there is no edge.
    Example:
    -  A  B  C  D
    A  0  1  0  0
    B  1  0  0  1
    C  0  1  1  0
    D  0  0  0  1
    """

    def __init__(self, size):
        self.size = size

        self.graph_matrix: list[list[int]] = [[0] * size for _ in range(size)]
        self.warshall_matrix: list[list[int]] = [[0] * size for _ in range(size)]
        self.routing_matrix: list[list[int]] = [[0] * size for _ in range(size)]
        self.floyd_warshall_matrix: list[list[int | float]] = [[0] * size for _ in range(size)]
        self.dfs_matrix: list[int] = [0] * size

        self._paths_created = False

    def reset_edges(self):
        """Set all the graph edges to 0."""
        for x in range(self.size):
            for y in range(self.size):
                self.graph_matrix[x][y] = 0  # Lack of the edge between x and y.

    def add_new_edge(self, x, y):
        """Add a new edge between `x` and `y`."""
        self._check_possible_exceptions(x, y)
        self.graph_matrix[x][y] = 1  # Edge between x and y exists now.

    def get_edge(self, x, y):
        """Returns 1 if the edge between `x` and `y` exists, 0 otherwise."""
        self._check_possible_exceptions(x, y)
        return self.graph_matrix[x][y]

    def print_graph(self, gtype, description=""):
        if gtype == "graph":
            matrix = self.graph_matrix
        elif gtype == "warshall":
            matrix = self.warshall_matrix
        elif gtype == "routing":
            matrix = self.routing_matrix
        else:
            raise MatrixGraphException("Unknown graph type.")

        """Prints the graph in a readeable way. First column - `x`. First row - `y`."""
        print(description)
        for x in range(self.size + 1):
            if x == 0:
                print(f"{'-':<2}", end=" ")
                for y in range(self.size):
                    print(f"{y:<2}", end=" ")
            else:
                print(f"{x-1:<2}", end=" ")
                for y in range(self.size):
                    print(f"{matrix[x - 1][y]:<2}", end=" ")
            print()
        print()

    def warshall(self):
        """Performs the Warshall algorithm. G[x][y] = 1 if the traversal from `x` to `y`
        is possible or G[x][y] = 0 if not. See `warshall_matrix` attribute."""
        self.warshall_matrix = deepcopy(self.graph_matrix)
        for x in range(self.size):
            for y in range(self.size):
                for z in range(self.size):
                    if self.warshall_matrix[y][z] == 0:
                        self.warshall_matrix[y][z] = self.warshall_matrix[y][x] * self.warshall_matrix[x][z]

    def create_paths(self):
        """Creates paths between all nodes of the graph. R[x][y] = 0 if there is no path between
        `x` and `y` and R[x][y] = z, where `z` denotes the following node on the path from `x` to `y`.
        See `routing_matrix` attribute. """
        self._init_routing_matrix()
        for x in range(self.size):
            for y in range(self.size):
                if self.routing_matrix[y][x] != 0:  # We know how to traverse from x to y.
                    for z in range(self.size):
                        if self.routing_matrix[y][z] == 0 and self.routing_matrix[x][z] != 0:
                            self.routing_matrix[y][z] = self.routing_matrix[y][x]
        self._paths_created = True

    def print_path(self, x, y):
        """Prints out the path from `x` to `y`."""
        if not self._paths_created:
            raise MatrixGraphException("Paths have not been created yet.")
        if self.routing_matrix[x][y] == 0:
            raise MatrixGraphException("Path does not exist.")
        k = self.routing_matrix[x][y]
        print(k, " ", end=" ")
        while k != y:
            k = self.routing_matrix[k][y]
            print(k, " ", end=" ")
        print()

    def floyd_warshall(self):
        """Perform the Floyd-Warshall algorithm of the shortest path."""
        self._reset_routing_matrix()
        self._init_floyd_warshall()

        for k in range(self.size):
            for i in range(self.size):
                for j in range(self.size):
                    if self.floyd_warshall_matrix[i][k] + self.floyd_warshall_matrix[k][j] < self.floyd_warshall_matrix[i][j]:
                        self.floyd_warshall_matrix[i][j] = self.floyd_warshall_matrix[i][k] + self.floyd_warshall_matrix[k][j]
                        self.routing_matrix[i][j] = k

    def floyd_warshall_path(self, i, j):
        """Prints out the shortest path between `i` and `j`."""
        k = self.routing_matrix[i][j]
        if k != 0:
            self.floyd_warshall_path(i, k)
            print(k, end="   ")
            self.floyd_warshall_path(k, j)

    def dfs_search(self):
        """Perform DFS algorithm. This function traverses through the graph accordingly to DFS.
        Normally we have to add some a comparison in such a function to find what we want."""
        for i in range(self.size):
            if self.dfs_matrix[i] == 0:
                self._dfs_traverse(i)

    def _dfs_traverse(self, i):
        self.dfs_matrix[i] = 1  # Node has been explored.
        print("Explore node:", i)
        for k in range(self.size):
            # There is an edge and the node hasn't been explored.
            if self.graph_matrix[i][k] != 0 and self.dfs_matrix[k] == 0:
                self._dfs_traverse(k)

    def _init_floyd_warshall(self):
        """Initialize floyd warshall matrix."""
        for x in range(self.size):
            for y in range(self.size):
                if self.graph_matrix[x][y] != 0:
                    self.floyd_warshall_matrix[x][y] = self.graph_matrix[x][y]
                else:
                    self.floyd_warshall_matrix[x][y] = float("inf")

    def _reset_routing_matrix(self):
        """Resets the routing matrix fields to 0."""
        for x in range(self.size):
            for y in range(self.size):
                self.routing_matrix[x][y] = 0

    def _init_routing_matrix(self):
        """Initialize the routing matrix."""
        for x in range(self.size):
            for y in range(self.size):
                if self.graph_matrix[x][y] == 0:
                    self.routing_matrix[x][y] = 0
                else:
                    self.routing_matrix[x][y] = y

    def _check_possible_exceptions(self, x, y):
        if x < 0 or x >= self.size:
            raise MatrixGraphException("The `x` is out of range.")
        if y < 0 or y >= self.size:
            raise MatrixGraphException("The `y` is out of range.")


def composition(G1, G2):
    """Returns graph which is composition of G1 and G2. The new graph contains
    all edges of G1 and all edges of G2."""
    if not G1.size == G2.size:
        return NotImplemented

    G3 = MatrixGraph(G1.size)
    for x in range(G3.size):
        for y in range(G3.size):
            z = 0
            while True:
                if z == G3.size:
                    break
                if G1.graph_matrix[x][z] == 1 and G2.graph_matrix[z][y] == 1:
                    G3.graph_matrix[x][y] = 1
                z += 1
    return G3


class MatrixGraphException(Exception):
    """Raises this exception when the module is used in invalid way."""
    pass
