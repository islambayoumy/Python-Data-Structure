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



"""
Method just for testing
"""
def test_func():
    cllist_node = CircularLinkedListNode()
    
    cllist_node.data = 1

    print(cllist_node.get_data())

test_func()
