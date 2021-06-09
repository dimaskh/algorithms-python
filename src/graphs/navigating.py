import networkx as nx
import matplotlib.pyplot as plt
from data import directed_graph

graph = nx.DiGraph(directed_graph)
pos = nx.spring_layout(graph)

nx.draw_networkx_labels(graph, pos)
nx.draw_networkx_nodes(graph, pos)
nx.draw_networkx_edges(graph, pos)

plt.savefig("src/graphs/figures/print/directed.png")

degrees_of_separation = nx.shortest_path_length(graph, 'A')
print('Degrees of separation: ', degrees_of_separation)
