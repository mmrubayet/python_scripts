# Defining "TreeNode" Python class
class TreeNode:
  def __init__(self, value):
    print("initializing node . . . ")
    self.value = value
    self.children = []

  def add_child(self, child_node):
    print("Adding " + child_node.value)
    self.children.append(child_node)

  def remove_child(self, child_node):
    print(f"Removing {child_node.value} from {self.value}")
    new_children = []
    for node in self.children:
      if node != child_node:
        new_children.append(node)
    self.children = new_children

root = TreeNode("I am Root")
child = TreeNode("A wee sappling")
bad_seed = TreeNode("Root Rot!")

root.add_child(child)
root.add_child(bad_seed)
root.remove_child(bad_seed)
