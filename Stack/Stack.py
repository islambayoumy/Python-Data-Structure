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
