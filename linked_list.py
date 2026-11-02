class Node:
    """
    Represents a data storage with a pointer to the next Node.

    Attributes:
        data (any): The data stored in a node.
        next (node): The next node in the linked list.
    """
    def __init__(self, data:any):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node object containing {self.data}.'

class LinkedList:
    """
    Attributes:
        head (node): The start of the linked list.

    Methods:
        add_right (node) -> None
        add_left (node) -> None
        pop_right () -> Node
        pop_left () -> Node
        contains (any) -> Boolean # Is there a node in here with that data?
    """
    def __init__(self):
        self.head = None

    def add_right(self, node_to_add: Node) -> None:
        """
        Adds a node to the tail of the LinkedList.
        """
        # Check if node_to_add is anything other than a Node or a child class of Node.
        if not isinstance(node_to_add, Node):
            data_to_add = node_to_add
            node_to_add = Node(data_to_add)
        # Adds a node as the head if there is no head.
        if not self.head:
            self.head = node_to_add
        else:
            # Find the tail.
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            tail = current_node
            # Make the node to add come next after the tail.
            tail.next = node_to_add

    def add_left(self, node_to_add: Node):
        """
        Adds a node as the head of the LinkedList.
        """
        # Check if node_to_add is anything other than a Node or a child class of Node.
        if not isinstance(node_to_add, Node):
            data_to_add = node_to_add
            node_to_add = Node(data_to_add)
        # Adds a node as the head if there is no head.
        if not self.head:
            self.head = node_to_add
        else:
            prior_head = self.head
            self.head = node_to_add
            self.head.next = prior_head

    def pop_left(self) -> Node:
        """
        Removes a node at the beginning of the LinkedList.
        """
        node_to_return = self.head
        self.head = self.head.next
        node_to_return.next = None
        return node_to_return

    def pop_right(self) -> Node:
        """
        Removes a node at the end of the LinkedList.
        """
        # Find the tail.
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        tail = current_node

    def __repr__(self):
        result = ''
        # If there is no head, it should look like "None".
        if not self.head:
            result = 'None'
        # Adds the arrow to the end of a node, if there is no node after the previous node, it will print "None".
        else: 
            current_node = self.head
            while current_node != None:
                result += f'{current_node.data} -> '
                current_node = current_node.next
            result += "None"
        return result

# Both Linked List class and Node are required to make a linked list.

# Diagram: Head -> Node -> Node -> ... -> None

linky = LinkedList()

for c in 'ABCDEFGHIJKLMNOP':
    linky.add_right(c)

linky.pop_left()

print(linky)