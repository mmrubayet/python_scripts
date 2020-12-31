print("Once upon a time . . .")
######
# TREENODE CLASS
######

class TreeNode:
  def __init__(self, story_piece):
    self.story_piece = story_piece
    self.choices = []

######
# VARIABLES FOR TREE
######

story = \
    """
    You are in a forest clearing. There is a path to the left.
    A bear emerges from the trees and roars!
    Do you:
    1 ) Roar back!
    2 ) Run to the left...
    """

story_root = TreeNode(story)

######
# TESTING AREA
######

print(story_root.story_piece)
