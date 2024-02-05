from node import Node

# I have only defined the parts of LinkedList that I need to use.
# I know there are other parts of it.(insert_end, stringify_list, remove_node)

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)

  def get_head_node(self):
    return self.head_node

  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node

  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list

  def print(self):
    current_node = self.get_head_node()
    while current_node is not None:
      print(f"{current_node.get_value()}", end=" ")
      current_node = current_node.get_next_node()
    print()