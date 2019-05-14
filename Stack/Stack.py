# Stack Data Structure [FILO]


class Stack:
    def __init__(self):
        self.items = list()

    def push(self, item):
        """
        Pushing new item to the top of the stack
        """
        self.items.append(item)
        return

    def pop(self):
        """
        Pop the top item of the stack
        """
        return self.items.pop()

    def is_empty(self):
        """
        Checking if the stack is empty?
        """
        return len(self.items) == 0

    def get_length(self):
        """
        Return length of the stack
        """
        return len(self.items)

    def get_stack(self):
        """
        return the stack
        """
        return self.items


"""
Method just for testing
"""


def test_func():  # pragma: no cover
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.get_stack())

    print(stack.pop())

    print(stack.get_length())

    print(stack.is_empty())


test_func()
