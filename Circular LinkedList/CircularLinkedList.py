# Circular Linked List


class CircularLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):  # pragma: no cover
        """
        Return data/value inside Node
        """
        return self.data

    def get_next(self):  # pragma: no cover
        """
        Return the pointer to the Next Node
        """
        return self.next


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def list_count(self):
        """
        Return number of Nodes in the LinkedList
        """
        current = self.head
        if not current:
            return 0
        else:
            count = 1
            while current.next != self.head:
                count += 1
                current = current.next
            return count

    def get_head(self):
        """
        Return head of LinkedList
        """
        return self.head

    def get_tail(self):
        """
        Return tail of LinkedList
        """
        current = self.head
        while current.next != self.head:
            current = current.next
        return current

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

    def delete_node(self, key):
        """
        Delete a specified node from the LinkedList by key
        """
        current = self.head
        if self.head.data == key:
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            current = None
        else:
            prev = None
            while current.next != self.head:
                prev = current
                current = current.next
                if current.data == key:
                    prev.next = current.next
                    current = None
                    break

        return self.head

    def print_list(self):  # pragma: no cover
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

    def has_cycle(self):
        """
        Determine whether the list has cycle or not.
        Cycle may occure between elements that don't include head
        """
        if not self.head:
            return False

        fast = self.head
        slow = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    def split_list(self, key):
        """
        splitting the list from a specified node into two lists
        and return head for each list
        """
        current = self.head
        prev = None

        if key == self.head.data:
            current = current.next
            self.head.next = self.head
        else:
            while current.data != key:
                prev = current
                current = current.next
            prev.next = self.head

        splited_list = CircularLinkedList()
        while current.next != self.head:
            splited_list.add_tail(current.data)
            current = current.next
        splited_list.add_tail(current.data)

        return self.head, splited_list.head


"""
Method just for testing
"""


def test_func():  # pragma: no cover
    cllist = CircularLinkedList()

    cllist.add_head(3)
    cllist.add_head(2)
    cllist.add_head(1)
    cllist.add_tail(4)
    cllist.add_tail(5)
    cllist.add_tail(6)

    head1, head2 = cllist.split_list(4)

    print(head1.data)
    print(head2.data)


test_func()
