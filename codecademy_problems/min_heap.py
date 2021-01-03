class MinHeap:
  def __init__(self):
    self.heap_list = [None]
    self.count = 0

  # define .add() below...
  def add(self, element):
    print(f"Adding {element} to {self.heap_list}")
