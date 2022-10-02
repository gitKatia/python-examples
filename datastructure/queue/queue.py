class Queue(object):

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def __len__(self):
        return self.size()

