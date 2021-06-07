from priority_queue import priority_queue
from data import weighted_graph

def prim(graph, start):
  treepath = {}
  total = 0
  queue = priority_queue()
  queue.push(0, (start, start))
  # print('Queue: ', queue.pop())
  while queue:
    weight, (node_start, node_end) = queue.pop()
    # print('sdfsd: ', weight, node_start, node_end)
    if node_end not in treepath:
      treepath[node_end] = node_start
      # print('treepath: ', treepath)
      if weight:
        # print('weight: ', weight)
        print("Added edge from %s to %s weighting %i" % (node_start, node_end, weight))
        total += weight
      for next_node, weight in graph[node_end].items():
        queue.push(weight, (node_end, next_node))

  print("Total spanning tree length: %i" % total)

  return treepath

treepath = prim(weighted_graph, 'A')
