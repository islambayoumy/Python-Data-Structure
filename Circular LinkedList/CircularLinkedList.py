# Circular Linked List

class CircularLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

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

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add_tail(self, data):
        """
        Insert new Node at the ending of the LinkedList
        """    
        node = CircularLinkedListNode(data)

        if not self.head:
            self.head = node
            self.head.next = self.head
            return
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = node
            node.next = self.head
            return

    def print_list(self):
        """
        Print the whole LinkedList
        """
        current = self.head
        while current:
            print(current.data)
            current = current.next
            if current == self.head:
                break
        return

"""
Method just for testing
"""
def test_func():
    cllist = CircularLinkedList()

    cllist.add_tail(1)
    cllist.add_tail(2)
    cllist.add_tail(3)

    cllist.print_list()

test_func()
