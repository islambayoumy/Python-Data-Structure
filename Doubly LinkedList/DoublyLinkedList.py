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

    def add_head(self, data):
        """
        Insert new Node at the beginning of the Doubly LinkedList
        """
        node = DoublyLinkedListNode(data)
        if not self.head:
            node.previous = None
            self.head = node
        else:
            self.head.previous = node
            node.next = self.head
            node.previous = None
            self.head = node

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

    def get_head(self):
        """
        Return head of LinkedList
        """
        return self.head

    def add_after(self, key, data):
        """
        Adding new node after given node
        """
        current = self.head
        while current:
            if not current.next and current.data == key:
                self.add_tail(data)
                return
            elif current.data == key:
                node = DoublyLinkedListNode(data)
                nxt = current.next
                current.next = node
                node.next = nxt
                node.previous = current
                nxt.previous = node

            current = current.next

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

    dllist.add_after(2, 5)


    dllist.print_list()

test_func()