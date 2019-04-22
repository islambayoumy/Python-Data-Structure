# Singly Linked List

class LinkedListNode:
        
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        """Return data/value inside Node"""
        return self.data

    def get_next(self):
        """Return the pointer to the Next Node"""
        return self.next


class LinkedList:

    def __init__(self):
        self.head = None
        self.count = 0

    def list_count(self):
        """Return number of Nodes in the LinkedList"""
        return self.count

    def add_head(self, data):
        """Insert new Node at the beginning of the LinkedList"""
        node = LinkedListNode(data)
        
        node.next = self.head
        self.head = node

        self.count+=1
        return
        
    def add_node(self, data, position):
        """Insert new Node at a specific position of the LinkedList"""        
        pre_node = self.get_node_by_position(position-1)            
        node = LinkedListNode(data)
        node.next = pre_node.next
        pre_node.next = node
        self.count+=1
        return
        
    def add_tail(self, data):
        """Insert new Node at the ending of the LinkedList"""    
        node = LinkedListNode(data)
        self.count+=1

        if self.head is None:
            self.head = node
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            return

    def get_head(self):
        """Return head of LinkedList"""
        return self.head
    
    def get_tail(self):
        """Return tail of LinkedList"""
        current = self.head
        while current.next:
            current = current.next
        return current

    def get_node_by_position(self, position):
        """Search a node by position"""
        if position <= 1:
            return self.get_head()
        elif 1 < position <= self.list_count():
            node = self.head
            for _ in range(0, position-1):
                node = node.next
            return node
        else:
            return self.get_tail()

    def get_node_by_data(self, data):
        """Search a node by data"""
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return

    def get_position_of_node_by_data(self, data):
        """Return position of first occurence of a data"""
        current = self.head
        position = 0
        while current:
            position+=1
            if current.data == data:
                return position
            current = current.next
        return
    
    def delete_head(self):
        """Delete the head of the LinkedList and return the new head"""
        node = self.head
        if node:
            self.head = node.next
            node = None
            self.count-=1
        return self.head

    def delete_by_position(self, position):
        """Delete a node of the LinkedList at certain position"""
        pre_node = self.get_node_by_position(position-1)
        node = pre_node.next
        
        if self.get_head() in [pre_node, node]:
            return self.delete_head()
        elif node:
            pre_node.next = node.next
            node = None
            self.count-=1
        return
    
    def delete_by_data(self, data):
        """Delete a node of the LinkedList by data"""
        node = self.get_node_by_data(data)
        node_position = self.get_position_of_node_by_data(data)
        pre_node = self.get_node_by_position(node_position-1)

        if self.get_head() in [pre_node, node]:
            return self.delete_head()
        elif node:
            pre_node.next = node.next
            node = None
            self.count-=1
        return

    def reverse_list_iterative(self):
        """Reverse the LinkedList iteratively"""
        pre_node = None
        curr_node = self.head
        while curr_node:
            nxt = curr_node.next
            curr_node.next = pre_node
            pre_node = curr_node
            curr_node = nxt
        self.head = pre_node
        return

    def reverse_list_recursive(self):
        """Reverse the LinkedList recursively"""
        def reverse_recursive(pre_node, curr_node):
            if not curr_node:
                return pre_node
            
            nxt = curr_node.next
            curr_node.next = pre_node
            pre_node = curr_node
            curr_node = nxt
            return reverse_recursive(pre_node, curr_node)

        self.head = reverse_recursive(None, self.head)
        return

    def print_list(self):
        """Print the whole LinkedList"""
        current = self.head
        while current:
            print(current.data)
            current = current.next




def test_func():
    llist = LinkedList()
    llist.add_tail(1)
    llist.add_tail(2)
    llist.add_head(3)
    llist.add_node(4, 0)
    llist.add_node(1, -2)
    llist.add_node(6, 2)
    llist.add_tail(7)


    print("Number of Nodes: {}".format(llist.list_count()))
    llist.print_list()
    
    llist.reverse_list_recursive()

    print("Number of Nodes: {}".format(llist.list_count()))
    llist.print_list()

test_func()
