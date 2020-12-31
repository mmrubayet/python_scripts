print("Once upon a time . . .")
######
# TREENODE CLASS
######

class TreeNode:
  def __init__(self, story_piece):
    self.story_piece = story_piece
    self.choices = []

  def add_child(self, node):
    self.choices.append(node)

  def traverse(self):
    # assign story_node to self
    # print out story_node's story_piece
    # while story_node has choices:
      # get the user's choice using input()
      # if the choice is invalid
        # tell the user
      # if the choice is valid
        # set choice as the new story_node
    story_node = self
    print(story_node.story_piece)



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


story_a = \
"""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
"""

choice_a = TreeNode(story_a)


story_b = \
"""
You come across a clearing full of flowers.
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
"""

choice_b = TreeNode(story_b)

story_root.add_child(choice_a)
story_root.add_child(choice_b)



user_choice = input("What is your name? \n_> ")
print(f"\nWelcome {user_choice}!")

######
# TESTING AREA
######

story_root.traverse()
