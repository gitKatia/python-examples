from datastructure.node import Node


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail_node().next = new_node

    def as_list(self):
        node_list = []
        current_node = self.head
        while current_node:
            node_list.append(current_node)
            current_node = current_node.next
        return node_list

    def list_size(self):
        return len(self.as_list())

    def is_empty(self):
        return self.list_size() == 0

    def tail_node(self):
        if self.is_empty():
            return None
        return self.as_list()[-1]