# importing networkx
import networkx as nx
# importing matplotlib.pyplot
import matplotlib.pyplot as plt

g = nx.Graph()

g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(1, 4)
g.add_edge(1, 5)
g.add_edge(5, 6)
g.add_edge(5, 7)
g.add_edge(4, 8)
g.add_edge(3, 8)

# drawing in circular layout
nx.draw(g, with_labels = True)
plt.savefig("src/graphs/figures/print/filename1.png")

# clearing the current plot
plt.clf()

# drawing in planar layout
nx.draw_planar(g, with_labels = True)
plt.savefig("src/graphs/figures/print/filename2.png")

# clearing the current plot
plt.clf()

# drawing in random layout
nx.draw_random(g, with_labels = True)
plt.savefig("src/graphs/figures/print/filename3.png")

# clearing the current plot
plt.clf()

# drawing in specrtal layout
nx.draw_spectral(g, with_labels = True)
plt.savefig("src/graphs/figures/print/filename4.png")

# clearing the current plot
plt.clf()

# drawing in spring layout
nx.draw_spring(g, with_labels = True)
plt.savefig("src/graphs/figures/print/filename5.png")

# clearing the current plot
plt.clf()

# drawing in shell layout
nx.draw_shell(g, with_labels = True)
plt.savefig("src/graphs/figures/print/filename6.png")

# clearing the current plot
plt.clf()
