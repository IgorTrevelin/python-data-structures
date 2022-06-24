class SinglyLinkedList():

  class Node:
    def __init__(self, data):
      self.data = data
      self.next = None

    def set_next(self, node):
      self.next = node

    def get_next(self):
      return self.next

    def get_data(self):
      return self.data


  def __init__(self):
    self.head = None

  def add(self, value):
    new_node = self.Node(value)

    if self.head is None:
      self.head = new_node
    else:
      current_node = self.head

      while current_node.get_next() is not None:
        current_node = current_node.get_next()

      current_node.set_next(new_node)

  def remove_by_index(self, index):
    if index >= len(self):
      return

    i = 0
    previous_node = None
    current_node = self.head

    while i != index:
      previous_node = current_node
      current_node = current_node.get_next()
      i += 1

    if current_node == self.head:
      self.head = current_node.get_next()
    else:
      previous_node.set_next(current_node.get_next())

  def remove_by_value(self, value, one_shot = True):
    current_node = self.head
    previous_node = None

    if self.head.get_data() == value:
      self.head = self.head.get_next()
      return

    while current_node.get_next() is not None:
      previous_node = current_node
      current_node = current_node.get_next()

      if current_node.get_data() == value:
        previous_node.set_next(current_node.get_next())

        if one_shot:
          break

  def __len__(self):
    count = 0
    current_node = self.head

    if current_node is None:
      return count

    count += 1
    while current_node.get_next() is not None:
      count += 1
      current_node = current_node.get_next()

    return count

  def __str__(self):
    current_node = self.head
    _str = '['
    
    while current_node is not None:
      _str += str(current_node.get_data())

      if current_node.get_next() is not None:
        _str += ', '

      current_node = current_node.get_next()

    _str += ']'

    return _str