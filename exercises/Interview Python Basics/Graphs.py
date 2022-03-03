#                 Pros of Adjacency List
# An adjacency list is efficient in terms of storage because we only need to store the values for the edges.
# For a sparse graph with millions of vertices and edges, this can mean a lot of saved space.
# It also helps to find all the vertices adjacent to a vertex easily.

#                 Cons of Adjacency List
# Finding the adjacent list is not quicker than the adjacency matrix because all the connected nodes
# must be first explored to find them.


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
        pass


def main():

    # Create graph and edges
    graph = GraphAdjacenList()
    graph.add_node(0)
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)

    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(5, 2)

    graph.print_agraph()


if __name__ == "__main__":
    main()
