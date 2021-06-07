import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from bfs import bfs
from dfs import dfs
from data import graph1 as graph

Graph = nx.Graph()

for node in graph:
  Graph.add_nodes_from(node)
  for edge in graph[node]:
    Graph.add_edge(node, edge)

pos = {
  'A': [0.00, 0.50],
  'B': [0.25, 0.75],
  'C': [0.25, 0.25],
  'D': [0.75, 0.75],
  'E': [0.75, 0.25],
  'F': [1.00, 0.50]
}

nx.draw(Graph, pos, with_labels=True)
nx.draw_networkx(Graph, pos)
plt.savefig("src/graphs/figures/print/traversing1.png")

stepsBFS = bfs(graph, 'A')
print('\nBFS: ', stepsBFS)

stepsDFS = dfs(graph, 'A')
print('\nDFS: ', stepsDFS)
