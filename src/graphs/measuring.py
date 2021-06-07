import networkx as nx
import matplotlib.pyplot as plt

AGraph = nx.Graph()

Nodes = range(1, 5)
Edges = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 3), (1, 5)]

AGraph.add_nodes_from(Nodes)
AGraph.add_edges_from(Edges)

AGraph.add_node(6)
print(sorted(nx.connected_components(AGraph)))

AGraph.add_edge(1, 6)
print(sorted(nx.connected_components(AGraph)))

degrees = [val for (node, val) in nx.degree(AGraph)]
print("Degrees: ", degrees)

clustering = nx.clustering(AGraph)
print("Clustering: ", clustering)

centrality = nx.degree_centrality(AGraph)
print("Centrality: ", centrality)

AGraph.add_node(7)
closeness_centrality = nx.closeness_centrality(AGraph)
print("Closeness Centrality: ", closeness_centrality)

betweenness_centrality = nx.betweenness_centrality(AGraph)
print("Betweenness Centrality: ", betweenness_centrality)
