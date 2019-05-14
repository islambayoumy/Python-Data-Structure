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
        pop the top item of the stack
        """
        return self.items.pop()
