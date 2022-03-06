#                 Pros of Adjacency List
# An adjacency list is efficient in terms of storage because we only need to store the values for the edges.
# For a sparse graph with millions of vertices and edges, this can mean a lot of saved space.
# It also helps to find all the vertices adjacent to a vertex easily.

#                 Cons of Adjacency List
# Finding the adjacent list is not quicker than the adjacency matrix because all the connected nodes
# must be first explored to find them.


from unittest.mock import patch


class GraphAdjacenList:
    def __init__(self):
        self.nodes = []
        self.adj_list = {}

    # Add edges
    def add_edge(self, s, d):
        if s in self.nodes and d in self.nodes:
            if s in self.adj_list:
                self.adj_list[s].append(d)
            else:
                self.adj_list[s] = [d]
        else:
            print("Nodes not exist in graph")

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
        else:
            print(f'Node {node} already exists!')
    # Print the graph

    def print_agraph(self):
        for node in self.adj_list:
            print(f'{node} ----> {[i for i in self.adj_list[node]]}')

    def dfs(self, visited, node):  # function for dfs
        if node not in visited:
            print(node)
            visited.add(node)
            if node in self.adj_list:
                for neighbour in self.adj_list[node]:
                    self.dfs(visited,  neighbour)

    def bfs(self, visited, node):
        visited.append(node)
        queue = []  #
        queue.append(node)

        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            if s in self.adj_list:
                for neighbour in self.adj_list[s]:
                    if neighbour not in visited:
                        visited.append(neighbour)
                        queue.append(neighbour)
    # Queue horizontal - BFS
    # Stack vertical -  DFS


#                   Pros of Adjacency Matrix
# The basic operations like adding an edge, removing an edge, and checking whether there is an
# edge from vertex i to vertex j are extremely time efficient, constant time operations.

# If the graph is dense and the number of edges is large, an adjacency matrix should be the first choice.
# Even if the graph and the adjacency matrix is sparse, we can represent it using data structures for sparse matrices.

# The biggest advantage, however, comes from the use of matrices. The recent advances in hardware enable us to perform
#  even expensive matrix operations on the GPU.

# By performing operations on the adjacent matrix, we can get important insights into the nature of the graph and the
# relationship between its vertices.


# Cons of Adjacency Matrix
# The VxV space requirement of the adjacency matrix makes it a memory hog. Graphs out in the wild usually don't have
# too many connections and this is the major reason why adjacency lists are the better choice for most tasks.

# While basic operations are easy, operations like inEdges and outEdges are expensive when using the adjacency matrix
# representation.
class GraphAdjMatrix:
    pass

    def __init__(self) -> None:
        self.adjMatrix = []
        self.size = 0
        self.vertices_no = 0
        self.vertices = []

    def add_node(self, node):
        if node not in self.vertices:
            self.vertices_no += 1
            self.vertices.append(node)
            if self.vertices_no > 1:
                for vertice in self.adjMatrix:
                    vertice.append(0)
            temp = []
            for i in range(self.vertices_no):
                temp.append(0)
            self.adjMatrix.append(temp)
        else:
            print(f'Node {node} already exists!')

    def add_edge(self, v1, v2, e):
        # Check if vertex v1 is a valid vertex
        if v1 not in self.vertices:
            print("Vertex ", v1, " does not exist.")
        # Check if vertex v1 is a valid vertex
        elif v2 not in self.vertices:
            print("Vertex ", v2, " does not exist.")
        # Since this code is not restricted to a directed or
        # an undirected graph, an edge between v1 v2 does not
        # imply that an edge exists between v2 and v1
        else:
            index1 = self.vertices.index(v1)
            index2 = self.vertices.index(v2)
            self.adjMatrix[index1][index2] = e

    def print_graph(self):
        for i in range(self.vertices_no):
            for j in range(self.vertices_no):
                if self.adjMatrix[i][j] != 0:
                    print(self.vertices[i], " -> ", self.vertices[j],
                          " edge weight: ", self.adjMatrix[i][j])


def main():

    # Create graph and edges
    graph_list = GraphAdjacenList()
    graph_list.add_node(0)
    graph_list.add_node(1)
    graph_list.add_node(2)
    graph_list.add_node(3)
    graph_list.add_node(4)
    graph_list.add_node(5)

    graph_list.add_edge(0, 1)
    graph_list.add_edge(0, 2)
    graph_list.add_edge(0, 3)
    graph_list.add_edge(3, 5)

    graph_list.add_edge(1, 2)
    graph_list.add_edge(5, 2)

    graph_list.print_agraph()

    visited = set()
    graph_list.dfs(visited, 0)
    print("DFS", visited)

    visited = []
    graph_list.bfs(visited, 0)
    print("BFS", visited)

    graph_matrix = GraphAdjMatrix()
    graph_matrix.add_node(6)
    graph_matrix.add_node(7)
    graph_matrix.add_node(8)
    graph_matrix.add_node(9)
    graph_matrix.add_node(10)
    graph_matrix.add_node(11)

    graph_matrix.add_edge(6, 7, 1)
    graph_matrix.add_edge(6, 8, 2)
    graph_matrix.add_edge(6, 9, 3)
    graph_matrix.add_edge(10, 7, 4)
    graph_matrix.add_edge(11, 10, 5)
    graph_matrix.print_graph()


  #
if __name__ == "__main__":
    main()
