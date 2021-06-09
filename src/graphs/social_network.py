import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community import k_clique_communities

graph = nx.karate_club_graph()

pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True)
plt.savefig("src/graphs/figures/print/social_network.png")

# Finding and printing all cliques of four
cliques = nx.find_cliques(graph)
print('All cliques of four: %s' % [c for c in cliques if len(c) >= 4])

# Joining cliques of four into communities
communities = k_clique_communities(graph, k=4)
communities_list = [list(c) for c in communities]
nodes_list = [node for community in communities_list for node in community]
print('Found these communities: %s' % communities_list)

# Printing the subgraph of communities
subgraph = graph.subgraph(nodes_list)
nx.draw(subgraph, with_labels=True)
plt.savefig("src/graphs/figures/print/social_network_communities.png")
