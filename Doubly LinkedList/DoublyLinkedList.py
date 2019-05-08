class DoublyLinkedListNode:
        
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def get_data(self):
        """
        Return data/value inside Node
        """
        return self.data

    def get_next(self):
        """
        Return the pointer to the Next Node
        """
        return self.next

    def get_previous(self):
        """
        Return the pointer to the Previous Node
        """
        return self.previous


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def add_tail(self, data):
        """
        Insert new Node at the ending of the Doubly LinkedList
        """
        node = DoublyLinkedListNode(data)
        if not self.head:
            node.previous = None
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = node
            node.previous = current
            node.next = None

    def get_tail(self):
        """
        Return tail of LinkedList
        """
        current = self.head
        while current.next:
            current = current.next
        return current

    def print_list(self):
        """
        Print the whole LinkedList
        """
        current = self.head
        while current:
            print(current.data)
            current = current.next
        return


"""
Method just for testing
"""
def test_func():
    dllist = DoublyLinkedList()

    dllist.add_tail(1)
    dllist.add_tail(2)
    dllist.add_tail(3)

    dllist.print_list()

test_func()