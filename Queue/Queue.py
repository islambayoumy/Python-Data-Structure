# Queue Data Structure [FIFO]


class Queue:
    def __init__(self):
        self.items = list()

    def enqueue(self, item):
        """
        Add new item to the end of the queue
        """
        self.items.insert(0, item)
        return

    def dequeue(self):
        """
        Return and remove first item from the queue
        """
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        """
        Checking if the queue is empty?
        """
        return len(self.items) == 0

    def get_max(self):
        """
        Return max in the queue
        """
        if not self.is_empty():
            return max(self.items)

    def queue_len(self):
        """
        Return length of the queue
        """
        len(self.items)

    def get_queue(self):  # pragma: no cover
        """
        Return the queue
        """
        return self.items

    def get_first(self):
        """
        Return first item added to the queue
        """
        if not self.is_empty():
            return self.items[-1]

    def get_last(self):
        """
        Return last item added to the queue
        """
        if not self.is_empty():
            return self.items[0]


"""
Method just for testing
"""


def test_func():  # pragma: no cover
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q.get_queue())

    print(q.dequeue())

    q.enqueue(4)
    q.enqueue(5)

    print(q.get_queue())

    print(q.get_first())
    print(q.get_last())


test_func()
