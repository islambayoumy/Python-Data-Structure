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
        if len(self.items):
            return False
        return True

    def get_length(self):
        """
        Return length of the stack
        """
        return len(self.items)