from find_path import find_path

graph = {
  'A': ['B', 'F'],
  'B': ['A', 'C'],
  'C': ['B', 'D'],
  'D': ['C', 'E'],
  'E': ['D', 'F'],
  'F': ['E', 'A'],
}

find_path(graph, 'B', 'E')
