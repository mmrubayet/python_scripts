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
    story_node = self   # assign story_node to self
    print(story_node.story_piece)   # print out story_node's story_piece

    while story_node.choices != []:   # while story_node has choices:
      choice = int(input("Enter 1 or 2 to continue the story: "))    # get the user's choice using input()
      if not choice in [1, 2]:    # if the choice is invalid
        print("Invalid Choice! Please enter 1 or 2: ")    # tell the user
      else:      # if the choice is valid
        chosen_index = choice - 1
        chosen_child = story_node.choices[chosen_index]
        print(chosen_child.story_piece)

        story_node = chosen_child     # set choice as the new story_node


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
