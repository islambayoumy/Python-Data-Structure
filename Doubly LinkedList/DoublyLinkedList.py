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

