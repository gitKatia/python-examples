from datastructure.queue.item import Item
from datastructure.queue.queue import Queue

if __name__ == '__main__':
    apple = Item("apple")
    queue = Queue()
    queue.enqueue(apple)
    queue.enqueue(apple)
    print(len(queue))

