from priority_queue import priority_queue
from data import weighted_graph

def kruskal(graph):
  priority = priority_queue()
  print("Pushing all edges into the priority queue")
  treepath = list()
  connected = dict()
  total = 0

  for node in graph:
    connected[node] = node
    for dest, weight in graph[node].items():
      priority.push(weight, (node, dest))

  print("Totally %i edges" % len(priority))
  print("Connected components: %s" % connected.values())

  while len(treepath) < (len(graph) - 1):
    (weight, (start, end)) = priority.pop()
    if end not in connected[start]:
      treepath.append((start, end))
      print("Summing %s and %s components:" % (connected[start], connected[end]))
      print("\tAdded edge from %s to %s weighting %i" % (start, end, weight))
      total += weight
      connected[start] += connected[end][:]
      for element in connected[end]:
        connected[element] = connected[start]

  print("Total spanning tree length: %i" % total)

  return sorted(treepath, key=lambda x:x[0])

print("\nMinimum spanning tree: %s" % kruskal(weighted_graph))
