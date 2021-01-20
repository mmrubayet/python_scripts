
graph = {
  'A': [('B', 10), ('C', 3)],
  'B': [('C', 3), ('D', 2)],
  'C': [('D', 2)],
  'D': [('E', 10)],
  'E': [('B', 15)],
}


for vertex in graph:
  print("\n\nVertex {0} connects to: ".format(vertex))
  for edge in graph[vertex]:
    print("vertex {0} with a weight of {1}".format(edge[0], edge[1]))
