import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from bfs import bfs
from dfs import dfs
from data import graph, positions

Graph = nx.Graph()

for node in graph:
  Graph.add_nodes_from(node)
  for edge in graph[node]:
    Graph.add_edge(node, edge)

nx.draw(Graph, positions, with_labels=True)
nx.draw_networkx(Graph, positions)
plt.savefig("src/graphs/figures/print/traversing1.png")

stepsBFS = bfs(graph, 'A')
print('\nBFS: ', stepsBFS)

stepsDFS = dfs(graph, 'A')
print('\nDFS: ', stepsDFS)
