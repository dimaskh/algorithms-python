import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from data import weighted_graph, positions

Graph = nx.Graph()
for node in weighted_graph:
  Graph.add_nodes_from(node)
  for edge, weight in weighted_graph[node].items():
    Graph.add_edge(node, edge, weight=weight)

labels = nx.get_edge_attributes(Graph, 'weight')
nx.draw(Graph, positions, with_labels=True)
nx.draw_networkx_edge_labels(Graph, positions, edge_labels=labels)
plt.savefig("src/graphs/figures/print/weighted.png")
