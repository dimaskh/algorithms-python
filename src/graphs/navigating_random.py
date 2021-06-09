from networkx import nx
from navigating import graph
import random
random.seed(0)

paths = nx.all_simple_paths(graph, 'A', 'H')

path_list = []
for path in paths:
  path_list.append(path)
  print('Path Candidate: ', path)

selected_path = random.randint(0, len(path_list) - 1)

print("The selected path is: ", path_list[selected_path])
