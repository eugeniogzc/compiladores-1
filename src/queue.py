class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, element):
        self._items.append(element)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

