import networkx as nx
import matplotlib.pyplot as plt

AGraph = nx.Graph()

Nodes = range(1, 5)
Edges = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 3), (1, 5)]

AGraph.add_nodes_from(Nodes)
AGraph.add_edges_from(Edges)

nx.draw(AGraph, with_labels=True)
plt.savefig("src/graphs/figures/init.png")
