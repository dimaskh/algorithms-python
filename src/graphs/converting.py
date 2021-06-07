import networkx as nx
import matplotlib.pyplot as plt

AGraph = nx.Graph()

Nodes = range(1, 6)
Edges = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 3), (1, 5), (1, 6)]

AGraph.add_nodes_from(Nodes)
AGraph.add_edges_from(Edges)

matrix = nx.to_numpy_matrix(AGraph)
print("Matrix: ", matrix)

sparse_matrix = nx.to_scipy_sparse_matrix(AGraph)
print("Sparse Matrix: ", sparse_matrix)

dict_of_lists = nx.to_dict_of_lists(AGraph)
print("Dictionary of Lists: ", dict_of_lists)
