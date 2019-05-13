# Singly Linked List


class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self): # pragma: no cover
        """
        Return data/value inside Node
        """
        return self.data

    def get_next(self): # pragma: no cover
        """
        Return the pointer to the Next Node
        """
        return self.next


class LinkedList:

    def __init__(self):
        self.head = None
        self.count = 0

    def list_count(self, node):
        """
        Return number of Nodes in the LinkedList
        """
        if not node:
            return 0
        return 1 + self.list_count(node.next)

    def add_head(self, data):
        """
        Insert new Node at the beginning of the LinkedList
        """
        node = LinkedListNode(data)

        node.next = self.head
        self.head = node

        self.count += 1
        return

    def add_node(self, data, position):
        """
        Insert new Node at a specific position of the LinkedList
        """
        pre_node = self.get_node_by_position(position-1)
        node = LinkedListNode(data)
        node.next = pre_node.next
        pre_node.next = node
        self.count += 1
        return

    def add_tail(self, data):
        """
        Insert new Node at the ending of the LinkedList
        """
        node = LinkedListNode(data)
        self.count += 1

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
        """
        Return head of LinkedList
        """
        return self.head

    def get_tail(self):
        """
        Return tail of LinkedList
        """
        current = self.head
        while current.next:
            current = current.next
        return current

    def get_node_by_position(self, position):
        """
        Search a node by position
        """
        if position <= 1:
            return self.get_head()
        elif 1 < position <= self.list_count(self.head):
            node = self.head
            for _ in range(0, position-1):
                node = node.next
            return node
        else:
            return self.get_tail()

    def get_node_by_data(self, data):
        """
        Search a node by data
        """
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return

    def get_position_of_node_by_data(self, data):
        """
        Return position of first occurence of a data
        """
        current = self.head
        position = 0
        while current:
            position += 1
            if current.data == data:
                return position
            current = current.next
        return

    def delete_head(self):
        """
        Delete the head of the LinkedList and return the new head
        """
        node = self.head
        if node:
            self.head = node.next
            node = None
            self.count -= 1
        return self.head

    def delete_by_position(self, position):
        """
        Delete a node of the LinkedList at certain position
        """
        pre_node = self.get_node_by_position(position-1)
        node = pre_node.next

        if self.get_head() in [pre_node, node]:
            return self.delete_head()
        elif node:
            pre_node.next = node.next
            node = None
            self.count -= 1
        return

    def delete_by_data(self, data):
        """
        Delete a node of the LinkedList by data
        """
        node = self.get_node_by_data(data)
        node_position = self.get_position_of_node_by_data(data)
        pre_node = self.get_node_by_position(node_position-1)

        if self.get_head() in [pre_node, node]:
            return self.delete_head()
        elif node:
            pre_node.next = node.next
            node = None
            self.count -= 1
        return

    def reverse_list_iterative(self):
        """
        Reverse the LinkedList iteratively
        """
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
        """
        Reverse the LinkedList recursively
        """
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

    def print_list(self): # pragma: no cover
        """
        Print the whole LinkedList
        """
        current = self.head
        while current:
            print(current.data)
            current = current.next
        return

    def swap_nodes(self, node_data1, node_data2):
        """
        Swap two adjacent nodes
        """
        if node_data1 == node_data2:
            return

        pre_node1 = None
        curr_node1 = self.head
        while curr_node1 and curr_node1.data != node_data1:
            pre_node1 = curr_node1
            curr_node1 = curr_node1.next

        pre_node2 = None
        curr_node2 = self.head
        while curr_node2 and curr_node2.data != node_data2:
            pre_node2 = curr_node2
            curr_node2 = curr_node2.next

        if not curr_node1 or not curr_node2:
            return

        if pre_node1:
            pre_node1.next = curr_node2
        else:
            self.head = curr_node2

        if pre_node2:
            pre_node2.next = curr_node1
        else:
            self.head = curr_node1

        curr_node1.next, curr_node2.next = curr_node2.next, curr_node1.next

    def merge_two_sorted_lists(self, mlist):
        head_list1 = self.head
        head_list2 = mlist.head
        newlist = None

        if not head_list1:
            return head_list2
        if not head_list2:
            return head_list1

        if head_list1 and head_list2:
            if head_list1.data <= head_list2.data:
                newlist = head_list1
                head_list1 = newlist.next
            else:
                newlist = head_list2
                head_list2 = head_list2.next
            newhead = newlist

        while head_list1 and head_list2:
            if head_list1.data <= head_list2.data:
                newlist.next = head_list1
                newlist = head_list1
                head_list1 = newlist.next
            else:
                newlist.next = head_list2
                newlist = head_list2
                head_list2 = newlist.next

        if not head_list1:
            newlist.next = head_list2
        if not head_list2:
            newlist.next = head_list1

        return newhead

    def remove_duplicates(self):
        """
        Removing duplicate data
        """
        current = self.head
        previous = None
        dupl_values = list()

        while current:
            if current.data in dupl_values:
                previous.next = current.next
                current = None
            else:
                dupl_values.append(current.data)
                previous = current
            current = previous.next

    def compare_two_lists_is_equal(self, head2):
        """
        Check if two linkedlists are identically equals
        """
        current1 = self.head
        current2 = head2

        if not current1 and not current2:
            return 1

        count1 = self.list_count(current1)
        count2 = self.list_count(current2)

        if count1 != count2:
            return 0

        while current1 and current2:
            if current1.data != current2.data:
                return 0
            current1 = current1.next
            current2 = current2.next
        return 1

    def count_occurence(self, data):
        """
        Count number of occurence of a value
        """
        count = 0
        current = self.head
        while current:
            if current.data == data:
                count += 1
            current = current.next
        return count

    def rotate_list(self, k):
        """
        Rotating the list to kth
        """
        p = self.head
        q = self.head

        previous = None
        count = 0

        while p and count < k:
            previous = p
            p = p.next
            q = q.next
            count += 1

        p = previous

        while q:
            previous = q
            q = q.next

        q = previous
        q.next = self.head
        self.head = p.next
        p.next = None

    def is_palindrome(self):
        """
        Check if the list is palindrome
        (could be read the same from both sides)
        """
        s = ""
        current = self.head

        while current:
            s += current.data
            current = current.next

        return s == s[::-1]

    def move_tail_to_head(self):
        """
        Move tail of the list to head
        """
        current = self.head
        pre_tail = None

        while current.next:
            pre_tail = current
            current = current.next

        current.next = self.head
        self.head = current
        pre_tail.next = None
        return

"""
Method just for testing
"""


def test_func(): # pragma: no cover
    llist = LinkedList()

    llist.add_tail("A")
    llist.add_tail("B")
    llist.add_tail("C")
    llist.add_tail("D")

    llist.move_tail_to_head()

    llist.print_list()

test_func()
