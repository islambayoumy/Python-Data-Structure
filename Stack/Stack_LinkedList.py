# Stack Data Structure [FILO]
# Implementation using LinkedList DS


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.oldMax = None


class Stack:
    def __init__(self):
        self.peek = None
        self.maximum = None

    def push(self, item):
        """
        Pushing new item to the top of the stack
        """
        node = Node(item)
        node.next = self.peek
        self.peek = node

        if not self.maximum or item > self.maximum:
            node.oldMax = self.maximum
            self.maximum = item

        return

    def pop(self):
        """
        Pop the top item of the stack
        """
        if not self.is_empty():
            temp = self.peek
            self.peek = self.peek.next

            if temp.oldMax:
                self.maximum = temp.oldMax

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

    def get_max(self):
        """
        Return max value in the stack
        """
        if self.is_empty():
            return None
        return self.maximum


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

    print(stack.get_max())
    stack.pop()
    print(stack.get_max())
    stack.pop()
    print(stack.get_max())


test_func()
