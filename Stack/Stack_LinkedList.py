# Stack Data Structure [FILO]
# Implementation using LinkedList DS


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.peek = None

    def push(self, item):
        """
        Pushing new item to the top of the stack
        """
        node = Node(item)
        node.next = self.peek
        self.peek = node
        return

    def pop(self):
        """
        Pop the top item of the stack
        """
        if not self.is_empty():
            temp = self.peek
            self.peek = self.peek.next
            return temp.data

    def is_empty(self):
        """
        Checking if the stack is empty?
        """
        return self.peek is None

    def get_peek(self):
        """
        Return peek of stack
        """
        return self.peek.data

    def stack_len(self, item):
        """
        Return number of items in the stack
        """
        if not item:
            return 0
        return 1 + self.stack_len(item.next)

    def get_stack(self):
        """
        Return stack as list
        """
        stack = list()
        current = self.peek
        while current:
            stack.append(current.data)
            current = current.next
        return stack


"""
Method just for testing
"""


def test_func():  # pragma: no cover
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    print(stack.get_stack())


test_func()
