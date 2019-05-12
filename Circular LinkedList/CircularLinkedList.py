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

    def add_head(self, data):
        """
        Insert new Node at the beginning of the LinkedList
        """
        node = CircularLinkedListNode(data)
        
        current = self.head
        node.next = self.head

        if not self.head:
            node.next = node
        else:
            while current.next != self.head:
                current = current.next
            current.next = node

        self.head = node
        return

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

    cllist.add_head(1)
    cllist.add_head(2)
    cllist.add_head(3)

    cllist.print_list()

test_func()
