class DoublyLinkedList:

  class Node:
    """
    Represents a DoublyLinkedList node
    """

    def __init__(self, data):
      self.data = data
      self.previous = None
      self.next = None

    def get_next(self):
      """
      Returns the next node pointer value
      """
      return self.next

    def set_next(self, next):
      """
      Changes the next node pointer value
      """
      self.next = next

    def get_previous(self):
      """
      Returns the previous node pointer value
      """
      return self.previous

    def set_previous(self, previous):
      """
      Changes the previous node pointer value
      """
      self.previous = previous

    def get_data(self):
      """
      Returns the data value of the node
      """
      return self.data

    def set_data(self, value):
      """
      Changes the node data value
      """
      self.data = value


  def __init__(self):
    self.head = None
    self.length = 0
    self.head = None

  def push(self, value):
    """
    Inserts new node at the beginning of the list
    """
    new_node = self.Node(value)
    current_node = self.head

    if current_node is None:
      self.head = new_node
    else:
      new_node.set_next(current_node)
      current_node.set_previous(new_node)
      self.head = new_node

    self.length += 1

  def append(self, value):
    """
    Inserts new node at the end of the list
    """
    new_node = self.Node(value)
    current_node = self.head

    if current_node is None:
      self.head = new_node
    else:
      while current_node.get_next() is not None:
        current_node = current_node.get_next()

      current_node.set_next(new_node)
      new_node.set_previous(current_node)

    self.length += 1

  def remove_by_index(self, index):
    """
    Removes element by index
    """
    if index < 0 or index >= self.length:
      raise IndexError('List index out of bounds')

    i = 0
    current_node = self.head

    while i != index:
      current_node = current_node.get_next()
      i += 1

    if current_node == self.head:
      self.head = current_node.get_next()
      if self.head is not None:
        self.head.set_previous(None)
    else:
      if current_node.get_next() is not None:
        current_node.get_next().set_previous(current_node.get_previous())
      current_node.get_previous().set_next(current_node.get_next())

    self.length -= 1

  def remove_by_value(self, value, single_value = True):
    """
    Removes element by value
    """
    current_node = self.head

    while current_node != None:
      if current_node.get_data() == value:
        if current_node == self.head:
          self.head = current_node.get_next()
          if self.head is not None:
            self.head.set_previous(None)
        else:
          if current_node.get_next() is not None:
            current_node.get_next().set_previous(current_node.get_previous())
          current_node.get_previous().set_next(current_node.get_next())

        self.length -= 1

        if single_value:
          break

      current_node = current_node.get_next()


  def get_by_index(self, index):
    """
    Returns the data value of the node at the specified index
    """
    if index < 0 or index >= self.length:
      raise IndexError('List index out of bounds')

    i = 0
    current_node = self.head

    while i < index:
      current_node = current_node.get_next()
      i += 1

    return current_node.get_data()

  def index_of(self, value):
    """
    Returns the node index of the first occurrence of the value in the list. If the value doesn't exist in the list, returns -1
    """
    i = 0
    current_node = self.head

    if current_node.get_data() == value:
      return i

    while current_node.get_next() is not None:
      current_node = current_node.get_next()
      i += 1

      if current_node.get_data() == value:
        return i

    return -1

  def update_by_index(self, index, value):
    """
    Updates the data value of the node at the specified index of the list
    """

    if index < 0 or index >= self.length:
      raise IndexError('List index out of bounds')

    i = 0
    current_node = self.head

    if i == index:
      current_node.set_data(value)

    while current_node.get_next() is not None:
      current_node = current_node.get_next()
      i += 1

      if i == index:
        current_node.set_data(value)
        return

  def __len__(self):
    """
    Returns the current length of the list when the list is passed to len function
    """
    return self.length

  def __str__(self):
    """
    Returns textual notation of the list
    """
    current_node = self.head
    _str = '['
    
    while current_node is not None:
      _str += str(current_node.get_data())

      if current_node.get_next() is not None:
        _str += ', '

      current_node = current_node.get_next()

    _str += ']'

    return _str