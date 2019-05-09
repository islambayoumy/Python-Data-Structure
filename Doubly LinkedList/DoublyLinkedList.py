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
    
    def list_count(self, node):
        """
        Return number of Nodes in the LinkedList
        """
        if not node:
            return 0
        return 1 + self.list_count(node.next)

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

    def add_before(self, key, data):
        """
        Adding new node before given node
        """
        current = self.head
        while current:
            if not current.previous and current.data == key:
                self.add_head(data)
                return
            elif current.data == key:
                node = DoublyLinkedListNode(data)
                prev = current.previous

                prev.next = node
                current.previous = node
                node.next = current
                node.previous = prev
                
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

    def delete_node(self, key):
        """
        Delete a node of the LinkedList by given data
        """
        current = self.head
        while current:
            if current.data == key and current == self.head:
                if not current.next:
                    current = None
                    self.head = None
                    return
                else:
                    nxt = current.next
                    
                    current.next = None
                    nxt.previous = None
                    current = None
                    self.head = nxt
                    return
            elif current.data == key:
                if current.next:
                    nxt = current.next
                    prev = current.previous

                    prev.next = nxt
                    nxt.previous = prev
                    current.next = None
                    current.previous = None
                    current = None
                    return
                else:
                    prev = current.previous

                    prev.next = None
                    current.previous = None
                    current = None
                    return

            current = current.next

    def reverse_list(self):
        """
        Reverse the Doubly LinkedList iteratively
        """
        tmp = None
        current = self.head
        while current:
            tmp = current.previous
            current.previous = current.next
            current.next = tmp
            current = current.previous
        
        if tmp:
            self.head = tmp.previous


"""
Method just for testing
"""
def test_func():
    dllist = DoublyLinkedList()

    dllist.add_tail(1)
    dllist.add_tail(2)
    dllist.add_tail(3)
    dllist.add_tail(4)

    dllist.print_list()
    print("\n")
    
    dllist.reverse_list()

    dllist.print_list()

test_func()