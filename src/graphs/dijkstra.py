from priority_queue import priority_queue
from data import weighted_directed_graph

def dijkstra(graph, start, end):
  inf = float('inf')
  known = set()
  priority = priority_queue()
  path = {start: start}

  for vertex in graph:
    if vertex == start:
      priority.push(0, vertex)
    else:
      priority.push(inf, vertex)
  last = start

  while last != end:
    (weight, actual_node) = priority.pop()
    if actual_node not in known:
      for next_node in graph[actual_node]:
        upto_actual = priority.index[actual_node]
        upto_next = priority.index[next_node]
        to_next = upto_actual + graph[actual_node][next_node]
        if to_next < upto_next:
          priority.push(to_next, next_node)
          print("Found shortcut from %s to %s" % (actual_node, next_node))
          print("\tTotal length up so far: %i" % to_next)
          path[next_node] = actual_node

      last = actual_node
      known.add(actual_node)

  return priority.index, path

dist, path = dijkstra(weighted_directed_graph, 'A', 'F')

def reverse_path(path, start, end):
  progression = [end]

  while progression[-1] != start:
    progression.append(path[progression[-1]])

  return progression[::-1]

print("\nPath: ", reverse_path(path, 'A', 'F'))
print("Distances: ", dist)
