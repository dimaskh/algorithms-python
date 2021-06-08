import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from data import weighted_directed_graph, positions

Graph = nx.DiGraph()

for node in weighted_directed_graph:
  Graph.add_nodes_from(node)
  for edge, weight in weighted_directed_graph[node].items():
    Graph.add_edge(node, edge, weight=weight)

labels = nx.get_edge_attributes(Graph, 'weight')
nx.draw(Graph, positions, with_labels=True)
nx.draw_networkx_edge_labels(Graph, positions, edge_labels=labels)
nx.draw_networkx(Graph, positions)
plt.savefig("src/graphs/figures/print/weighted_directed.png")
