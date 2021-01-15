from vertex import Vertex

class Graph:
  def __init__(self):
    self.graph_dict = {}

  def add_vertex(self, node):
    self.graph_dict[node.value] = node

  def add_edge(self, from_node, to_node, weight = 0):
    self.graph_dict[from_node.value].add_edge(to_node.value, weight)
    self.graph_dict[to_node.value].add_edge(from_node.value, weight)

  def explore(self):
    print("Exploring the graph....\n")
    #FILL IN EXPLORE METHOD BELOW
    current_room = 'entrance'
    path_total = 0

    print(f"\nStarting off at the {current_room}\n")

    while current_room != 'treasure room':
      node = self.graph_dict[current_room]

      for connected_room, weight in node.edges.items():
        key = connected_room[0]
        print(f"enter {key} for {connected_room}: {weight} cost")
      valid_choices = [room[:1] for room in node.edges.keys()]
      print(f"\nYou have accumulated: {path_total} cost")
      choice = input("\nWhich room do you move to? ")



  def print_map(self):
    print("\nMAZE LAYOUT\n")
    for node_key in self.graph_dict:
      print("{0} connected to...".format(node_key))
      node = self.graph_dict[node_key]
      for adjacent_node, weight in node.edges.items():
        print("=> {0}: cost is {1}".format(adjacent_node, weight))
      print("")
    print("")

def build_graph():
  graph = Graph()

  # MAKE ROOMS INTO VERTICES BELOW...
  entrance = Vertex("entrance")

  # ADD ROOMS TO GRAPH BELOW...
  graph.add_vertex(entrance)

  ante_chamber = Vertex("ante-chamber")
  graph.add_vertex(ante_chamber)

  kings_room = Vertex("king's room")
  graph.add_vertex(kings_room)

  grand_gallery = Vertex("grand gallery")
  graph.add_vertex(grand_gallery)

  treasure_room = Vertex("treasure room")
  graph.add_vertex(treasure_room)


  # ADD EDGES BETWEEN ROOMS BELOW...
  graph.add_edge(entrance, ante_chamber, 7)
  graph.add_edge(entrance, kings_room , 3)
  graph.add_edge(kings_room, ante_chamber, 1)

  graph.add_edge(grand_gallery, ante_chamber, 2)
  graph.add_edge(grand_gallery, kings_room, 2)

  graph.add_edge(treasure_room, ante_chamber, 6)
  graph.add_edge(treasure_room, grand_gallery , 4)


  # DON'T CHANGE THIS CODE
  graph.print_map()
  return graph
