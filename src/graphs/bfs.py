def bfs(graph, start):
  queue = [start]
  queued = list()
  path = list()

  while queue:
    print('Queue is: %s' % queue)
    vertex = queue.pop(0)
    print('Processing %s' % vertex)

    for candidate in graph[vertex]:
      if candidate not in queued:
        queued.append(candidate)
        queue.append(candidate)
        path.append(vertex + '>' + candidate)
        print('Adding %s to the queue' % candidate)

  return path
