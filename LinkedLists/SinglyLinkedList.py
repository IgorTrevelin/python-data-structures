class SinglyLinkedList():

    class Node:
        """
        Represents a SinglyLinkedList node
        """

        def __init__(self, data):
            self.data = data
            self.next = None

        def set_next(self, node):
            """
            Changes the next node pointer value
            """
            self.next = node

        def get_next(self):
            """
            Returns the next node pointer value
            """
            return self.next

        def get_data(self):
            """
            Returns the node data value
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

    def push(self, value):
        """
        Inserts new node at the beginning of the list
        """
        new_node = self.Node(value)
        new_node.set_next(self.head)

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

        self.length += 1

    def remove_by_index(self, index):
        """
        Removes element by index
        """
        if index >= self.length or index < 0:
            raise IndexError('List index out of bounds')

        i = 0
        previous_node = None
        current_node = self.head

        while i != index:
            previous_node = current_node
            current_node = current_node.get_next()
            i += 1

        if current_node == self.head:
            self.head = current_node.get_next()
            del current_node
            current_node = self.head
        else:
            previous_node.set_next(current_node.get_next())
            del current_node
            current_node = previous_node.get_next()

        self.length -= 1

    def remove_by_value(self, value, single_value=True):
        """
        Removes element by value
        """
        current_node = self.head
        previous_node = None

        while current_node is not None:
            if current_node.get_data() == value:
                if current_node == self.head:
                    self.head = current_node.get_next()
                    del current_node
                    current_node = self.head
                else:
                    previous_node.set_next(current_node.get_next())
                    del current_node
                    current_node = previous_node.get_next()

                self.length -= 1

                if single_value:
                    break

            else:
                previous_node = current_node
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
