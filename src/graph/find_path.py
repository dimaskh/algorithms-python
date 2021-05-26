def find_path(graph, start, end, path = []):
  path = path + [start]
  print("Path ", path)

  if start == end:
    print("Ending")
    return path

  for node in graph[start]:
    print("Checking node ", node)

    if node not in path:
      print("Path so far ", path)

      newp = find_path(graph, node, end, path)
      if newp:
        return newp
